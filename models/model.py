import uuid
from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from datetime import datetime


class QRC (SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    is_winner: bool
    date_created: datetime = Field(default_factory=datetime.now)
    date_scanned: datetime | None = None
    url: str

class User (SQLModel):
    id: int
    name: str
    email: str
    password: str
    qr_code: list[QRC] = []

class Batch (SQLModel):
    id: int
    date_created: datetime = Field(default_factory=datetime.now)
    qr_list: list[QRC] = []