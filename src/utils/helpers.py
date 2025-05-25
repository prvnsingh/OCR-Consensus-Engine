from PIL import Image
import os

def load_images_from_folder(folder_path):
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            yield filename, Image.open(os.path.join(folder_path, filename)).convert("RGB")
