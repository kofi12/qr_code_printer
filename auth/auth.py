from fastapi import FastAPI, Request, Depends
from sqlmodel import Session
from models import db
from models.model import UserSchema
from datetime import datetime

async def create_new_user(request: Request, db: Session = Depends(db.get_session)):
    data = await request.json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

    import uuid

    # Need to make some changes within the models
    user = UserSchema(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        is_verified=False,
        )

    db.add(user)
    db.commit()
    return user