import PIL.Image
import pytest
from models.model import QRCode
from controller.qr_controller import *

@pytest.fixture
def test_data():
  return {
    'is_winner' : False
  }


def test_generate_qr(test_data) -> bool:
	qrcode = generate_qr(test_data)
	return isinstance(qrcode, PIL.Image)