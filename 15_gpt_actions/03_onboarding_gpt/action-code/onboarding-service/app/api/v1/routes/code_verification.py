from fastapi import APIRouter, HTTPException
from datetime import timedelta

from app.core import security
from app.api.deps import DBSessionDep
from app.core.config import logger_config
from app.models.base import Token, VerificationResponse
from app.crud.verification_codes import create_verification_code, get_verification_code, expire_verification_code
from app.crud.student import get_student_by_email
from app.core.utils import generate_verification_code, send_verification_code_email
from app.crud.student import verify_student_email
from app import settings

logger = logger_config(__name__)

router = APIRouter()


@router.post("/verification-code", response_model=VerificationResponse)
def get_verification_code_on_email(email: str, db: DBSessionDep):
    """
    Takes an email address and sends a verification code to the email address.
    State: Email 
    """
    try:
        is_student = get_student_by_email(session=db, email=email)
        if is_student is None:
            raise HTTPException(status_code=404, detail="Kindly Register First - No Student Records found for this email")
        # Generate the verification code
        code = generate_verification_code()

        # Save the code in the database
        create_verification_code(session=db, email=email, code=code)

        # Send the code via email (or SMS)
        send_verification_code_email(email_to=email, code=code)

        return VerificationResponse(message="Verification code sent. Please check your email.")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.post("/verify-code", response_model=Token)
def verify_code(code: str, db: DBSessionDep):
    """
    Takes a verification code and verifies it.
    For Valid Code:
        - Marks student as verified

    Returns:
        OAuth Tokens
    """
    try:
        db_code = get_verification_code(session=db, code=code)
        if db_code is None:
            raise HTTPException(
                status_code=404, detail="Invalid or expired code")

        expire_verification_code(db, db_code)

        verify_student_email(session=db, email=db_code.email)

        # Generate and return an authentication token for the session if needed
        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token_data = Token(
            access_token=security.create_access_token(
                db_code.email, expires_delta=access_token_expires
            ),
            expires_in=(settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
        )
        return token_data

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
