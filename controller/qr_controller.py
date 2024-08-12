from models.model import QRC, Batch
from models.db import get_session
from fastapi import Depends, status
from sqlmodel import Session, select
from fastapi.exceptions import HTTPException
import segno
from io import BytesIO
import base64

"""
    How to generate qrcodes using the qrcode library

    1. Read in qrcode data from the db
    2. convert the data into json if needed
    3. call qrcode.make(json_data)

"""

def generate_qr(batch_size: int,
                session: Session = Depends(get_session)):
    # need to add logic for random winner
    batch = Batch()
    session.add(batch)
    session.commit()
    batch_id = batch.id
    qr_codes = []

    for i in range(batch_size):
        q = QRC(batch_id=batch_id)
        session.add(q)
        session.commit()
        url = f"http://localhost:8000/codes/{q.id}"
        qr = segno.make(url)
        buffer = BytesIO()
        qr.save(buffer, kind = 'png')
        buffer.seek(0)
        qr_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        qr_codes.append(qr_base64)

    return {'qrcodes': qr_codes}


def get_qr_by_id(qr_id: int,
                 session: Session = Depends(get_session)):
    statement = select(QRC).where(QRC.id == qr_id)
    try:
        result = session.exec(statement)
        return result.first()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The qrcode does not exist")

def get_qrcodes(session: Session = Depends(get_session)):
    statement = select(QRC)
    return session.exec(statement).all()


