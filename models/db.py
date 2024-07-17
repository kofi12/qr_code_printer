from sqlmodel import Session, create_engine
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
DATABASE_URL = os.getenv('DATABASE_URL', '')
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session