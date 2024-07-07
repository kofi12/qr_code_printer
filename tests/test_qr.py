import pytest
import segno
from controller.qr_controller import *

def test_generate_qr():
	qrcode = generate_qr('Winner winner chicken dinner')
	assert isinstance(qrcode, segno.QRCode)
