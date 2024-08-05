from model import UserBase, UserDB

# API models
class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int