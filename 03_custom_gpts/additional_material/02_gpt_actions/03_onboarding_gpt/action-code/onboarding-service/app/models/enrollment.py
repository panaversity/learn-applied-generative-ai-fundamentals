from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import TYPE_CHECKING
from app.models.base import BaseIdModel, QuarterEnum, QuarterEnrollmentStatusEnum, FeeStatusEnum
from app.settings import PROGRAM_ID

if TYPE_CHECKING:
    from app.models.student import Student

##############################
#### Program Enrollments ####
##############################


class ProgramEnrollmentBase(SQLModel):
    student_id: UUID = Field(default=None, foreign_key="student.id")
    program_id: UUID = Field(default=PROGRAM_ID)
    program_name: str | None = Field(
        nullable=False, default="Certified Cloud Native Applied Generative AI Engineer")


class ProgramEnrollment(ProgramEnrollmentBase, BaseIdModel, table=True):
    student: "Student" = Relationship(back_populates="program_enrollments")
    quarter_enrollments: list["QuarterEnrollment"] = Relationship(
        back_populates="program_enrollment")


class ProgramEnrollmentCreate(ProgramEnrollmentBase):
    pass


class ProgramEnrollmentRead(ProgramEnrollmentBase):
    id: UUID
    program_id: UUID
    program_name: str


##############################
#### Quarter Enrollments ####
##############################

class QuarterEnrollmentBase(SQLModel):
    student_id: UUID | None = Field(default=None, foreign_key="student.id")
    program_enrollment_id: UUID = Field(foreign_key="programenrollment.id")
    quarter: QuarterEnum = Field(nullable=False, default=QuarterEnum.Q1)
    fee_amount: float = Field(nullable=False, default=4500.00)
    fee_status: FeeStatusEnum = Field(
        nullable=False, default=FeeStatusEnum.PENDING)
    quarter_enrollment_status: QuarterEnrollmentStatusEnum | None = Field(
        nullable=False, default=QuarterEnrollmentStatusEnum.PENDING)


class QuarterEnrollment(QuarterEnrollmentBase, BaseIdModel, table=True):
    student: "Student" = Relationship(back_populates="quarter_enrollments")
    program_enrollment: "ProgramEnrollment" = Relationship(
        back_populates="quarter_enrollments")


class QuarterEnrollmentCreate(QuarterEnrollmentBase):
    pass


class QuarterEnrollmentRead(QuarterEnrollmentBase):
    id: UUID


class PaginatedQuarterEnrollmentRead(SQLModel):
    count: int
    next: str | None = None
    previous: str | None = None
    all_records: list[QuarterEnrollmentRead]


##############################
#### API Data base Request Models ####
##############################

class StudentProgramEnrollmentResponse(SQLModel):
    checkout_url: str
    program_enrollment: ProgramEnrollmentRead
    quarter_enrollment: QuarterEnrollmentRead


class StudentQuarterEnrollmentResponse(SQLModel):
    checkout_url: str
    quarter_enrollment: QuarterEnrollmentRead


class PaymentLinkRequest(SQLModel):
    student_email: str
    program_id: UUID = Field(default=(PROGRAM_ID))
    quarter: QuarterEnum = Field(default=QuarterEnum.Q1)
    access_token: str
