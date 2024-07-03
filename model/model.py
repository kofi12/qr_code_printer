from pydantic import BaseModel


class QRCode (BaseModel):
    id: int
    is_winner: bool
    date_created: str
    date_scanned: str
    
class User (BaseModel) :
    id: int
    name: str
    email: str
    password: str
    qr_code: int