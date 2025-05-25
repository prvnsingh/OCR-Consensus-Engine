import easyocr
import numpy as np
from PIL import Image
from .base import OCREngine

class EasyOCREngine(OCREngine):
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image: Image.Image) -> str:
        results = self.reader.readtext(np.array(image), detail=0)
        return " ".join(results)
