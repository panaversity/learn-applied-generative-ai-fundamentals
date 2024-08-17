from typing import Optional
from sqlmodel import SQLModel, Field

class TodoBase(SQLModel):
    content: str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)