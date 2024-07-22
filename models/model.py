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

class User (SQLModel, table=True):
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    first_name: str
    last_name: str
    email: str
    password: str
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return f"<User {self.first_name}.{self.last_name}>"


class Batch (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)