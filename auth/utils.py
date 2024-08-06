from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi import Depends
from sqlmodel import Session
from ..models.db import get_session
import jwt
import json
from jwt import PyJWTError
import logging
import uuid
import bcrypt
import os
from dotenv import load_dotenv, find_dotenv

ACCESS_TOKEN_EXPIRY = 3600

load_dotenv(find_dotenv())
JWT_SECRET = os.getenv('JWT_SECRET', '')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', '')

def hash_passwd(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')

def verify_passwd(password: str, hash: str) -> bool:
    password_byte_enc = password.encode('utf-8')
    hash_byte_enc = hash.encode('utf-8')
    return bcrypt.checkpw(password = password_byte_enc , hashed_password = hash_byte_enc)

def authenticate_user(username: str, password: str,
                      session: Session = Depends(get_session)):
    from .users import get_user
    user = get_user(username, session)
    if not user:
        return False
    if not verify_passwd(password, user.hashed_password):
        return False
    return user

def create_access_token(user_data: dict, expiry: timedelta, refresh: bool = False):
    payload = {}
    if expiry:
        expire = datetime.now(timezone.utc) + expiry
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    payload['user'] = user_data
    payload['exp'] = expire.isoformat()
    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh

    token = jwt.encode(
        payload=payload,
        key=JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    return token

def decode_token(token: str) -> dict | None:

    try:
        token_data = jwt.decode(
            jwt=token,
            key=JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )
        return token_data
    except PyJWTError as e:
        logging.exception(e)
        return None
