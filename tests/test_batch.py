import pytest
from routes.routes import create_codes
from fastapi.testclient import TestClient
from sqlmodel import Session
from models.model import Batch, QRC
from models import db
from main import app

client = TestClient(app)

def test_create_batch():
    pass