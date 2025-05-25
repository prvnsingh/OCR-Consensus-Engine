import pytesseract
from PIL import Image
from .base import OCREngine

class PyTesseractEngine(OCREngine):
    def extract_text(self, image: Image.Image) -> str:
        return pytesseract.image_to_string(image, config='--psm 6').strip()
