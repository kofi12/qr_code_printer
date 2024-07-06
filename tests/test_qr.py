import pytest
from qrcode import image
from controller.qr_controller import *

def test_generate_qr() -> bool:
	qr_code = generate_qr('This is a test')
	return isinstance(qr_code, qrcode.image.pil.PilImage)