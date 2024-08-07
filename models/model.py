import uuid
from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime


class QRC (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_winner: bool = Field(default=False)
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
    created: datetime = Field(sa_column=Column(pg.TIMESTAMP), default_factory=datetime.now)
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None