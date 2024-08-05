from fastapi import FastAPI, Request, Depends, APIRouter
from sqlmodel import Session
from .users import create_user
from models.db import get_session
from models.model import UserDB
from models.schemas import UserCreate
from datetime import datetime

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/signup', response_model=UserDB)
def create_user_account(user_data: UserCreate,
                        session: Session = Depends(get_session)):
    return create_user(user_data, session)