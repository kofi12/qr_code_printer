from models.model import QRC
from fastapi import Request, Depends
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
    qrcode = segno.make(qr.model_dump_json())
    return qrcode

def get_qr_by_id():
    pass