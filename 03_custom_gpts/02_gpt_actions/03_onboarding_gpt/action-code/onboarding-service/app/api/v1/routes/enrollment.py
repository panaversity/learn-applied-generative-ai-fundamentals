from fastapi import APIRouter, HTTPException, Request, Body
from fastapi.responses import JSONResponse
import uuid

from app import settings
from app.api.deps import DBSessionDep, body_access_token

from app.core.config import logger_config
from app.core.stripe_session import generate_checkout_session
from app.crud.student import get_student_by_email

from app.crud.enrollment import (create_program_enrollment, create_quarter_enrollment, get_quarter_enrollments_by_student_email,
                                 update_quarter_enrollment_statuses, get_quarter_enrollment_by_id, get_quarter_enrollment_by_email_qnum, get_program_enrollment_by_email_pid)
from app.models.base import FeeStatusEnum, QuarterEnum, QuarterEnrollmentStatusEnum
from app.models.enrollment import (ProgramEnrollmentCreate, QuarterEnrollmentCreate, ProgramEnrollmentRead, StudentProgramEnrollmentResponse,
                                   QuarterEnrollmentCreate, PaginatedQuarterEnrollmentRead, StudentQuarterEnrollmentResponse, PaymentLinkRequest)

import stripe

logger = logger_config(__name__)

stripe.api_key = str(settings.STRIPE_SECRET_KEY)
stripe_webhook_secret = str(settings.STRIPE_WEBHOOK_SECRET)

router = APIRouter()


@router.post("/new", response_model=StudentProgramEnrollmentResponse)
async def student_new_program_and_course_enrollment(
    *,
    session: DBSessionDep,
    access_token: str = Body(embed=True),
):
    """
    - Enrolls the student in GenAI program.
    - Automatically enrolls the student in the first quarter after program enrollment.
    - Generates a Stripe checkout session URL for the first quarter fee payment.
    Response: - Returns enrollment details and checkout URL.
    """
    reg_stu = body_access_token(access_token)
    
    student = get_student_by_email(session=session, email=reg_stu.email)
    if not student:
        raise HTTPException(
            status_code=404, detail="Student not found in record - kindly register first")
    
    if student.email_verified is False:
        raise HTTPException(
            status_code=400, detail="Email not verified - please verify email")

    logger.info("Enrolling student in program")
    enrollment = create_program_enrollment(
        session=session, obj_in=ProgramEnrollmentCreate(student_id=student.id))

    logger.info("Automatically enroll the student in the first quarter")
    quarter_enrollment = create_quarter_enrollment(session=session,
                                                   obj_in=QuarterEnrollmentCreate(student_id=student.id, quarter=QuarterEnum.Q1, fee_status=FeeStatusEnum.PENDING, program_enrollment_id=enrollment.id))

    checkout_session = generate_checkout_session(
        quarter_enrollment=quarter_enrollment, student_email=reg_stu.email, enrollment=enrollment, quarter=1)

    # Return the program enrollment and the checkout URL
    return {
        "checkout_url": checkout_session['url'],
        "program_enrollment": enrollment,
        "quarter_enrollment": quarter_enrollment,
    }


@router.post("/new/quarter", response_model=StudentQuarterEnrollmentResponse)
async def student_new_quarter_enrollment(
    *,
    session: DBSessionDep,
    payment_link_request: PaymentLinkRequest
):
    """
    Manual Enrollment - Generates a Stripe checkout session URL for the quarter fee payment.
    Response: - Returns the quarter enrollment details and the checkout URL.
    """
    reg_stu = body_access_token(payment_link_request.access_token)
    
    if (reg_stu.email != payment_link_request.student_email):
        raise HTTPException(status_code=400, detail="Invalid email address")
    
    student_email = payment_link_request.student_email
    program_id = payment_link_request.program_id
    quarter = payment_link_request.quarter

    student = get_student_by_email(session=session, email=student_email)
    if not student or not student.id:
        raise HTTPException(
            status_code=404, detail="Student not found in record - kindly register first")
        
    if student.email_verified is False:
        raise HTTPException(
            status_code=400, detail="Email not verified - please verify email")

    # Get the program enrollment by student ID and program ID
    enrollment = get_program_enrollment_by_email_pid(
        session=session, student_id=student.id, program_id=program_id)
    
    if enrollment is None:
        raise HTTPException(
            status_code=404, detail="Program Enrollment not found")

    logger.info("Manually enroll the student in the specified quarter")
    quarter_enrollment = create_quarter_enrollment(session=session,
                                                   obj_in=QuarterEnrollmentCreate(student_id=student.id, quarter=quarter, fee_status=FeeStatusEnum.PENDING, program_enrollment_id=enrollment.id))

    checkout_session = generate_checkout_session(
        quarter_enrollment=quarter_enrollment, student_email=student_email, quarter=int(quarter.split("Q")[1]), enrollment=enrollment)

    # Return the program enrollment and the checkout URL
    return {
        "checkout_url": checkout_session['url'],
        "quarter_enrollment": quarter_enrollment,
    }


@router.post("/payment-link", response_model=StudentQuarterEnrollmentResponse)
async def get_new_payment_link(
    *,
    session: DBSessionDep,
    payment_link_request: PaymentLinkRequest,
):
    """
    Get Payment Link for the student based on email and quarter number
    """
    try:
        reg_stu = body_access_token(payment_link_request.access_token)
        if (reg_stu.email != payment_link_request.student_email):
            raise HTTPException(status_code=400, detail="Invalid email address")
        
        student_email = payment_link_request.student_email
        program_id = payment_link_request.program_id
        quarter = payment_link_request.quarter
        quarter_number = int(quarter.split("Q")[1])

        student = get_student_by_email(session=session, email=student_email)
        if not student:
            raise HTTPException(
                status_code=404, detail="Student not found in record - kindly register first")
            
        if student.email_verified is False:
            raise HTTPException(
                status_code=400, detail="Email not verified - please verify email first")

        # Get the program enrollment by student ID and program ID
        enrollment = get_program_enrollment_by_email_pid(
            session=session, student_id=student.id, program_id=program_id)
        
        if enrollment is None:
            raise HTTPException(status_code=404, detail="Program Enrollment not found")

        # Get the quarter enrollment by email and quarter number
        quarter_enrollment = get_quarter_enrollment_by_email_qnum(
            session=session, student_id=student.id, quarter=quarter_number
        )
        
        if quarter_enrollment is None:
            raise HTTPException(status_code=404, detail="Quarter Enrollment not found")

        # If Fee Status is PAID, return the quarter enrollment
        if quarter_enrollment.fee_status == FeeStatusEnum.PAID:
            return {
                "quarter_enrollment": quarter_enrollment,
                "checkout_url": "Payment already made for this quarter."
            }

        checkout_session = generate_checkout_session(
            quarter_enrollment=quarter_enrollment, student_email=student_email, quarter=quarter_number, enrollment=enrollment)

        # Return the program enrollment and the checkout URL
        return {
            "checkout_url": checkout_session['url'],
            "quarter_enrollment": quarter_enrollment,
        }

    except HTTPException as http_e:
        raise http_e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.get("/genai-program/{student_email}", response_model=ProgramEnrollmentRead)
def get_program_enrollments_for_student(*, session: DBSessionDep, student_email: str, page: int = 1, per_page: int = 10):
    student = get_student_by_email(session=session, email=student_email)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    enrollment = get_program_enrollment_by_email_pid(
        session=session, student_id=student.id, program_id=settings.PROGRAM_ID)
    
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Program Enrollment not found")
    
    return enrollment


@router.get("/genai-program/quarters/{student_email}", response_model=PaginatedQuarterEnrollmentRead)
def get_quarter_enrollments_for_student(*, session: DBSessionDep, student_email: str, page: int = 1, per_page: int = 10):
    student = get_student_by_email(session=session, email=student_email)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    enrollments = get_quarter_enrollments_by_student_email(
        session=session, student_id=student.id, offset=(page - 1) * per_page, limit=per_page)
    count = len(enrollments)
    next_page = f"?page={
        page + 1}&per_page={per_page}" if count == per_page else None
    previous_page = f"?page={
        page - 1}&per_page={per_page}" if page > 1 else None
    return PaginatedQuarterEnrollmentRead(count=count, next=next_page, previous=previous_page, all_records=enrollments)


@router.post("/webhook", include_in_schema=False)
async def stripe_webhook(request: Request, session: DBSessionDep):
    print("\n\n Webhook received \n\n ")
    print(request.headers)
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_webhook_secret
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        stripe_session = event['data']['object']
        quarter_enrollment_id = stripe_session['metadata']['quarter_enrollment_id']

        # Convert the quarter_enrollment_id from string to UUID
        quarter_enrollment_uuid = uuid.UUID(quarter_enrollment_id)

        # Get the quarter enrollment by ID
        quarter_enrollment = get_quarter_enrollment_by_id(
            session=session, quarter_enrollment_id=quarter_enrollment_uuid)
        if not quarter_enrollment:
            raise HTTPException(
                status_code=404, detail="Quarter Enrollment not found")

        # Update fee status to PAID and quarter enrollment status to ENROLLED
        quarter_enrollment.fee_status = FeeStatusEnum.PAID
        quarter_enrollment.quarter_enrollment_status = QuarterEnrollmentStatusEnum.ENROLLED
        update_quarter_enrollment_statuses(
            session=session, db_obj=quarter_enrollment)

    return JSONResponse(status_code=200, content={"received": True, "event": "checkout.session.completed"})
