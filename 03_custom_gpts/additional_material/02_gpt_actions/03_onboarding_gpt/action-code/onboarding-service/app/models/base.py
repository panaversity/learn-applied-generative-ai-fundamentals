from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

class BaseIdModel(SQLModel):
    id: UUID | None = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow, 
        sa_column_kwargs={"onupdate": datetime.now}
    )
    
# An Enum for Quarters 1 - 7
class QuarterEnum(str, Enum):
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"
    Q5 = "Q5"
    Q6 = "Q6"
    Q7 = "Q7"
    
# An Enum for Fee Status
class FeeStatusEnum(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    LATE = "late"
    
# Enum for Quarter Enrollment Status
class QuarterEnrollmentStatusEnum(str, Enum):
    PENDING = "pending"
    ENROLLED = "enrolled"
    COMPLETED = "completed"
    DROPPED = "dropped"
    DEFERRED = "deferred"

# Token Models
class Token(SQLModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int
    
# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None

class DecodedTokenPayload(SQLModel):
    email: str
    
class VerificationResponse(SQLModel):
    message: str