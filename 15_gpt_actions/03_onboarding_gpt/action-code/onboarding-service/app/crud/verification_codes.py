from sqlmodel import Session, select
from fastapi import HTTPException
from typing import Optional
from datetime import datetime, timedelta

from app.models.verification_codes import VerificationCode, VerificationCodeCreate


def create_verification_code(session: Session, email: str, code: str) -> VerificationCode:
    try:
        expiry = datetime.utcnow() + timedelta(minutes=15)
        obj_in = VerificationCodeCreate(email=email, code=code, expiry=expiry)
        db_obj = VerificationCode.model_validate(obj_in)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


def get_verification_code(session: Session, code: str) -> Optional[VerificationCode]:
    try:
        item_in_db = session.exec(select(VerificationCode).where(
            VerificationCode.code == code
        )).first()
        if item_in_db is None or item_in_db.used or item_in_db.expiry < datetime.utcnow():
            raise HTTPException(
                status_code=404, detail="Verification code not found or expired")
        return item_in_db
    except HTTPException as e:
        raise e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


def expire_verification_code(session: Session, verification_code_obj: VerificationCode) -> VerificationCode:
    try:
        verification_code_obj.used = True
        session.add(verification_code_obj)
        session.commit()
        return verification_code_obj
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
