from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from models.db import engine
from routes.qr_routes import qr_router
from routes.auth_route import auth_router

app = FastAPI()
SQLModel.metadata.create_all(engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(qr_router)
app.include_router(auth_router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}