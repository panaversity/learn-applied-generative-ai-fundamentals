from fastapi import APIRouter, HTTPException

from app.api.deps import DBSessionDep
from app.core.config import logger_config
from app import settings
from app.models.base import VerificationResponse, FeeStatusEnum
from app.models.student import Student, StudentCreate, StudentStatus
from app.crud.student import get_student_by_email, create_student
from app.crud.verification_codes import create_verification_code
from app.core.utils import generate_verification_code, send_verification_code_email
from app.crud.enrollment import get_quarter_enrollment_by_email_qnum, get_program_enrollment_by_email_pid

logger = logger_config(__name__)

router = APIRouter()


@router.get("/{email}", response_model=StudentStatus)
def check_student_onboarding_status_by_email(email: str, session: DBSessionDep):
    """
    Returns Student Onboarding Status.
    Args: email
    Returns:
    StudentStatus:
        - registration_status: (bool)
        - email_verified: (bool)
        - program_enrollment_status:(bool)
        - quarter_enrollment_status:(bool)
        - payment_status:(bool)
    """
    student = get_student_by_email(session=session, email=email)

    if student is None or student.id is None:
        return StudentStatus(
            registration_status=False,
            email_verified=False,
            program_enrollment_status=False,
            quarter_enrollment_status=False,
            payment_status=False
        )

    # If email_verified is False, return the student status
    if not student.email_verified:
        return StudentStatus(
            registration_status=True,
            email_verified=student.email_verified,
            program_enrollment_status=False,
            quarter_enrollment_status=False,
            payment_status=False
        )

    # Get the program enrollment by student ID and program ID
    enrollment = get_program_enrollment_by_email_pid(
        session=session, student_id=student.id, program_id=settings.PROGRAM_ID)

    if enrollment is None:
        return StudentStatus(
            registration_status=True,
            email_verified=student.email_verified,
            program_enrollment_status=False,
            quarter_enrollment_status=False,
            payment_status=False
        )

    # Get the quarter enrollment by email and quarter number
    quarter_enrollment = get_quarter_enrollment_by_email_qnum(
        session=session, student_id=student.id, quarter=1
    )
    if quarter_enrollment is None:
        return StudentStatus(
            registration_status=True,
            email_verified=student.email_verified,
            program_enrollment_status=True,
            quarter_enrollment_status=False,
            payment_status=False
        )

    # If Fee Status is PAID, return the quarter enrollment
    if quarter_enrollment.fee_status == FeeStatusEnum.PAID:
        return StudentStatus(
            registration_status=True,
            email_verified=student.email_verified,
            program_enrollment_status=True,
            quarter_enrollment_status=True,
            payment_status=True
        )

    return StudentStatus(
        registration_status=True,
        email_verified=student.email_verified,
        program_enrollment_status=True,
        quarter_enrollment_status=True,
        payment_status=False
    )


@router.post("/", response_model=VerificationResponse)
async def create_new_student(session: DBSessionDep, student_in: StudentCreate):
    """
    Register a new student and send a verification email.

    Args:
        student_in (StudentCreate):Info to be registered.

    Returns:
        VerificationResponse: text telling a verification code has been sent.

    Raises:
        HTTPException: For error occurs during registration.

    """
    logger.info(f"Creating student in database: {Student.__name__}")
    try:
        student = get_student_by_email(session=session, email=student_in.email)
        
        if student and student.email_verified is False:
            return VerificationResponse(message="Student already exists. Please verify email to continue")
        
        if student and student.email_verified:
            return VerificationResponse(message="Student already exists. Please login to continue.")

        created_student = create_student(session=session, obj_in=student_in)

        if settings.SMTP_PASSWORD is not None:
            # Generate the verification code
            code = generate_verification_code()

            # Save the code in the database
            create_verification_code(
                session=session, email=created_student.email, code=code)

            # Send the code via email (or SMS)
            send_verification_code_email(
                email_to=created_student.email, code=code)

        # return created_student
        return VerificationResponse(message="Verification code sent. Please check your email and share Code to complete Registration.")

    except HTTPException as http_e:
        raise http_e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
