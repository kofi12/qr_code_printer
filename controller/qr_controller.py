from ..models.model import QRC
from ..models.db import get_session
from fastapi import Request, Depends, status
from sqlmodel import Session, select
from fastapi.exceptions import HTTPException
import segno
import pyzbar
import json

"""
    How to generate qrcodes using the qrcode library

    1. Read in qrcode data from the db
    2. convert the data into json if needed
    3. call qrcode.make(json_data)

"""

def generate_qr(qr: QRC) -> segno.QRCode:
    url = f"http://localhost:8000/generate/{qr.id}"
    qrcode = segno.make(qr.model_dump_json())
    return qrcode

def get_qr_by_id(qr_id: int,
                 session: Session = Depends(get_session)):
    statement = select(QRC).where(QRC.id == qr_id)
    try:
        result = session.exec(statement)
        return result.first()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The qrcode does not exist")
