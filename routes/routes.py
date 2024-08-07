from fastapi import APIRouter, Request, Depends
from sqlmodel import Session, select
from ..models import db
from ..models.model import Batch, QRC
from ..controller.qr_controller import get_qr_by_id
import pyzbar

router = APIRouter(prefix='/api')

@router.post("/create-batch")
async def create_codes(request: Request, db: Session = Depends(db.get_session)):
    data = await request.json()
    num_codes = data['number']

    batch = Batch()
    db.add(batch)
    db.commit()
    db.refresh(batch)

    for i in range(num_codes):
        qrcode = QRC(is_winner=False, batch_id=batch.id)
        db.add(qrcode)
    db.commit()

    return batch

@router.get("/codes")
def get_codes(db: Session = Depends(db.get_session)):
    qrcodes = []
    qrcodes = db.exec(select(QRC)).all()
    return qrcodes

@router.get('/display-codes')


@router.get("/codes/{id}")
def get_code_by_id(id: int, request: Request, session: Session = Depends(db.get_session)) -> QRC | None:
    return get_qr_by_id(id, session)

@router.get("/decode/{id}")
def decode(request: Request):
    pass
