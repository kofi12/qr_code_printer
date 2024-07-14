from fastapi import APIRouter, Request, Depends
from models import model, db

router = APIRouter(prefix='/api')

@router.post("/generate-qr")
async def create_codes(request: Request):
    data = await request.json()
    num_codes = data['number']

    pass

@router.get("/decode")
def decode(request: Request):
    pass

