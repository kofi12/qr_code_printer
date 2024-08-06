from .model import UserBase, UserDB
from pydantic import BaseModel

# API models
class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class UserLogin(BaseModel):
    email: str
    password: str