from fastapi import Depends, APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlmodel import Session
from .users import create_user, get_user_by_email
from ..models.db import get_session
from ..models.model import UserDB
from ..models.schemas import UserCreate, UserLogin
from .utils import create_access_token, decode_token, verify_passwd
from datetime import timedelta

REFRESH_TOKEN_EXPIRY = 2

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/signup', response_model=UserDB)
def create_user_account(user_data: UserCreate,
                        session: Session = Depends(get_session)):
    return create_user(user_data, session)

@auth_router.post('/login')
def login_user(login_data: UserLogin,
               session: Session = Depends(get_session)):
    email = login_data.email
    password = login_data.password

    user = get_user_by_email(email, session)

    if user and verify_passwd(password, user.hashed_password):

        user_data = user.model_dump(exclude={'created'})
        access_token = create_access_token(
            user_data=user_data,
            expiry=timedelta(seconds=3600)
        )

        refresh_token = create_access_token(
            user_data=user_data,
            expiry=timedelta(days=REFRESH_TOKEN_EXPIRY),
            refresh= True
        )

        return JSONResponse(
            content={
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_info":user_data   # how much user_data should I return, should hashed_password also be excluded
            }
        )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password"
    )