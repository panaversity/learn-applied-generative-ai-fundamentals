from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime

from app.models.base import BaseIdModel

class VerificationCodeBase(SQLModel):
    email: str = Field(max_length=320, nullable=False)
    code: str = Field(max_length=6, nullable=False, unique=True)
    expiry: datetime = Field(nullable=False)
    used: bool = Field(default=False)


class VerificationCode(VerificationCodeBase, BaseIdModel, table=True):
    pass


class VerificationCodeCreate(VerificationCodeBase):
    pass

