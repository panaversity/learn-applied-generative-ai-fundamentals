from sqlmodel import Session, select
from fastapi import HTTPException
from typing import Optional
from app.models.student import Student, StudentCreate


def create_student(session: Session, *, obj_in: StudentCreate) -> Student:
    """
    Create a new Item in the database
    Args:
        obj_in: New Item to create (from request body)
        session: Session: Database session
    Returns:
        obj_in: Item that was created (with Id and timestamps included)
    """
    try:
        db_obj = Student.model_validate(obj_in)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    except HTTPException as http_e:
        session.rollback()
        raise http_e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


def get_student_by_email(session: Session, email: str) -> Optional[Student]:
    try:
        return session.exec(select(Student).where(Student.email == email)).first()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# Takes Email and Mark student email_status as verified


def verify_student_email(session: Session, email: str) -> Student:
    try:
        db_obj = get_student_by_email(session=session, email=email)
        if db_obj is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db_obj.email_verified = True
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    except HTTPException as http_e:
        session.rollback()
        raise http_e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
