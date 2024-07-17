from fastapi import APIRouter, Request, Depends
from sqlmodel import Session, select
from controller.qr_controller import generate_qr
from models import db
from models.model import Batch, QRC

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

    return batch.date_created

@router.get("/codes")
def get_codes(db: Session = Depends(db.get_session)):
    qrcodes = []
    qrcodes = db.exec(select(QRC)).all()
    return qrcodes


@router.get("/codes/{id}")
def get_code_by_id(id: int, request: Request, db: Session = Depends(db.get_session)):
    qrcode = db.exec(select(QRC).where(QRC.id == id))
    return qrcode

@router.get("/decode/{id}")
def decode(request: Request):
    pass

