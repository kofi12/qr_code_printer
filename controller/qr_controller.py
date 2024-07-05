import PIL.Image
from models.model import QRCode
import qrcode
import pyzbar
import json

"""
    How to generate qrcodes using the qrcode library

    1. Read in qrcode data from the db
    2. convert the data into json if needed
    3. call qrcode.make(json_data)

"""

async def generate_qr(qr: QRCode):
    data = json.dumps(qr)
    return qrcode.make(data)