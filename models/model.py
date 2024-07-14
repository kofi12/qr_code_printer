import uuid
from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from datetime import datetime


class QRC (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_winner: bool
    batch_id: int | None = Field(default=None, foreign_key='batch.id')

class User (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    new: str

class Batch (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date_created: datetime = Field(default_factory=datetime.now)