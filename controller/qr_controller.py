import PIL
from model import QRcode, User
import qrcode
import pyzbar
import json

"""
    How to generate qrcodes using the qrcode library
    
    1. Read in qrcode data from the db
    2. convert the data into json if needed
    3. call qrcode.make(json_data)
        
"""

async def generate_qr(**qr: QRcode) -> PIL.Image.Image:
    data = qr.json()
    return qrcode.make(data)