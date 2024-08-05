from fastapi import Depends, status
from sqlmodel import Session, select
from models.model import UserDB
from models.schemas import UserCreate
from .utils import hash_passwd, verify_passwd
from models.db import get_session
from fastapi.exceptions import HTTPException

#Define user functions, create, ect.

def create_user(user_data: UserCreate,
                session: Session = Depends(get_session)):
    user_data_dict = user_data.model_dump()

    if not user_exists(user_data, session):
        user = UserDB(
            **user_data_dict
        )
        user.hashed_password = hash_passwd(user_data_dict['password'])

        session.add(user)
        session.commit()

        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with email already exists")


#Helper methods
def user_exists(user_data: UserCreate,
                session: Session = Depends(get_session)) -> bool:
    user = get_user_by_email(user_data, session)
    if user is None:
        return False
    return True

def get_user_by_email(user_data: UserCreate,
                      session: Session = Depends(get_session)) -> UserDB | None:
    email = user_data.email
    statement = select(UserDB).where(UserDB.email == email)
    result = session.exec(statement)
    return result.first()


