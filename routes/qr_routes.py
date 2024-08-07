from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from ..models import db
from ..models.model import Batch, QRC
from ..controller.qr_controller import get_qr_by_id, get_qrcodes, generate_qr

qr_router = APIRouter(prefix='/api')

@qr_router.get("/create-batch/{batch_size}", response_class=JSONResponse)
async def create_codes(batch_size: int, request: Request, db: Session = Depends(db.get_session)):
    return generate_qr(batch_size, db)

@qr_router.get("/codes")
def get_codes(db: Session = Depends(db.get_session)):
    return get_qrcodes(db)

@qr_router.get('/display-codes')


@qr_router.get("/codes/{id}")
def get_code_by_id(id: int, request: Request, session: Session = Depends(db.get_session)) -> QRC | None:
    return get_qr_by_id(id, session)

