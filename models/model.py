import uuid
from pydantic import BaseModel, Field
from sqlalchemy import TIMESTAMP
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime


class QRC (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_winner: bool
    batch_id: int | None = Field(default=None, foreign_key='batch.id')

class Batch (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)

class UserBase(SQLModel):
    username: str = Field(index=True)
    email: str = Field(unique=True, index=True)

# Database model
class UserDB(UserBase, table=True):
    __tablename__ :str = "users"
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str

# API models
class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int