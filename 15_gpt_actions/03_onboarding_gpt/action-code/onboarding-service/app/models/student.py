from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from app.models.base import BaseIdModel

if TYPE_CHECKING:
    from app.models.enrollment import ProgramEnrollment, QuarterEnrollment


class StudentBase(SQLModel):
    name: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    phone_number: str = Field(nullable=False)
    country: str = Field(nullable=False)


class Student(StudentBase, BaseIdModel, table=True):
    email_verified: bool = Field(nullable=False, default=False)
    phone_number_verified: bool = Field(nullable=False, default=False)
    program_enrollments: list["ProgramEnrollment"] = Relationship(
        back_populates="student")
    quarter_enrollments: list["QuarterEnrollment"] = Relationship(
        back_populates="student")


class StudentCreate(StudentBase):
    pass


class StudentStatus(SQLModel):
    registration_status: bool = Field(default=False)
    email_verified: bool = Field(default=False)
    program_enrollment_status: bool = Field(default=False)
    quarter_enrollment_status: bool = Field(default=False)
    payment_status: bool = Field(default=False)
