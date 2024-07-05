import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class QRC (BaseModel):
    unique_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_winner: bool
    date_created: datetime = Field(default_factory=datetime.now)
    date_scanned: datetime | None = None

class User (BaseModel) :
    id: int
    name: str
    email: str
    password: str
    qr_code: list[QRC] = []