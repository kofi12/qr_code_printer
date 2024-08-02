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

# How can I ensure no missing arguments warnings
# when trying to insert a user without the id or dates


class Batch (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)

class UserSchema (BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_verified: bool = Field(default=False)