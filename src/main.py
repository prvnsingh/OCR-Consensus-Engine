import json
import logging
import os

from ocr_engines.easyocr_engine import EasyOCREngine
from ocr_engines.pytesseract_engine import PyTesseractEngine
from ocr_engines.trocr_engine import TrOCREngine
from utils.helpers import load_images_from_folder
from utils.discrepancy_resolver import resolve_discrepancy
import warnings

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("ocr_process.log"),
        logging.StreamHandler()
    ]
)

warnings.filterwarnings("ignore", category=UserWarning)


def main(image_folder: str, output_file: str):
    if not os.path.isdir(image_folder):
        logging.error(f"Image folder '{image_folder}' not found.")
        return

    engines = {
        'easyocr': EasyOCREngine(),
        'pytesseract': PyTesseractEngine(),
        'trocr': TrOCREngine()
    }

    final_results = []
    image_count = 0

    for img_name, img in load_images_from_folder(image_folder):
        logging.info(f"Processing image: {img_name}")
        ocr_outputs = {}
        for name, engine in engines.items():
            try:
                text = engine.extract_text(img)
                ocr_outputs[name] = text
                logging.debug(f"{name} output for {img_name}: {text[:100]}")
            except Exception as e:
                ocr_outputs[name] = ""
                logging.warning(f"[{name.upper()} ERROR] on {img_name}: {str(e)}")

        try:
            final_text = resolve_discrepancy(ocr_outputs)
            final_results.append({
                "image_name": img_name,
                "text": final_text
            })
            image_count += 1
        except Exception as e:
            logging.error(f"Failed to resolve discrepancy for {img_name}: {e}")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(final_results, f, indent=4, ensure_ascii=False)
        logging.info(f"Successfully saved results for {image_count} images to {output_file}")
    except Exception as e:
        logging.critical(f"Failed to save JSON output: {e}")

if __name__ == "__main__":
    main("../data", "../output/ocr_results.json")
