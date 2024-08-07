from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.enrollment import ProgramEnrollment, ProgramEnrollmentCreate, QuarterEnrollment, QuarterEnrollmentCreate
from app.models.base import FeeStatusEnum
from uuid import UUID


def create_program_enrollment(session: Session, *, obj_in: ProgramEnrollmentCreate) -> ProgramEnrollment:
    try:
        # Check if Student is already enrolled in the program
        db_obj_check = session.exec(select(ProgramEnrollment).where(ProgramEnrollment.student_id == obj_in.student_id, ProgramEnrollment.program_id == obj_in.program_id)).one_or_none()
        if db_obj_check:
            raise HTTPException(status_code=400, detail="Student is already enrolled in the program")
        
        db_obj = ProgramEnrollment.model_validate(obj_in)
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

def get_program_enrollment_by_email_pid(session: Session, student_id: UUID, program_id: UUID) -> ProgramEnrollment | None:
# Get Program Enrollment by Email and Program ID
    try:
        db_obj = session.exec(select(ProgramEnrollment).where(ProgramEnrollment.student_id == student_id, ProgramEnrollment.program_id == program_id)).one_or_none()
        if db_obj is None:
            return None
        return db_obj
    except HTTPException as http_e:
        session.rollback()
        raise http_e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

#### Quarter Enrollment CRUD Operations #### 
def create_quarter_enrollment(session: Session, *, obj_in: QuarterEnrollmentCreate) -> QuarterEnrollment:
    try:
        # Check if for this Quarter, Student is already enrolled
        db_obj_check = session.exec(select(QuarterEnrollment).where(QuarterEnrollment.student_id == obj_in.student_id, QuarterEnrollment.quarter == obj_in.quarter)).one_or_none()
        if db_obj_check:
            # If Fee Status is PENDING, then tell this in Error Message as well
            if db_obj_check.fee_status == FeeStatusEnum.PENDING:
                raise HTTPException(status_code=400, detail="Student is already enrolled in this quarter with PENDING Fee Status")
            else:
                raise HTTPException(status_code=400, detail="Student is already enrolled in this quarter")
        
        db_obj = QuarterEnrollment.model_validate(obj_in)
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

def get_quarter_enrollments_by_student_email(session: Session, student_id: UUID, *, offset: int = 0, limit: int = 100) -> list[QuarterEnrollment]:
    try:
        items = session.exec(select(QuarterEnrollment).where(QuarterEnrollment.student_id == student_id).offset(offset).limit(limit)).all()
        return items
    except HTTPException as http_e:
        session.rollback()
        raise http_e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

def update_quarter_enrollment_statuses(session: Session, db_obj = QuarterEnrollment) -> QuarterEnrollment:
    try:

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

def get_quarter_enrollment_by_id(session: Session, quarter_enrollment_id: UUID) -> QuarterEnrollment:
    try:
        db_obj = session.get(QuarterEnrollment, quarter_enrollment_id)
        if db_obj is None:
            raise HTTPException(status_code=404, detail="Quarter Enrollment not found")
        return db_obj
    except HTTPException as http_e:
        session.rollback()
        raise http_e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
    
def get_quarter_enrollment_by_email_qnum(session: Session, student_id: UUID, quarter: int) -> QuarterEnrollment | None:
    try:
        db_obj = session.exec(select(QuarterEnrollment).where(QuarterEnrollment.student_id == student_id, QuarterEnrollment.quarter == str(f'Q{quarter}'))).one_or_none()
        if db_obj is None:
            return None
        return db_obj
    except HTTPException as http_e:
        session.rollback()
        raise http_e
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")