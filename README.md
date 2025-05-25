# 🧠 OCR Consensus Engine

Extract text from images using multiple OCR engines (EasyOCR, PyTesseract, TrOCR), compare the results using Levenshtein similarity, and generate a consensus output with case sensitivity, punctuation, and spacing retained.

## 📦 Project Structure

```
ocr_consensus_project/
│
├── data/
│   └── images      # Input image dataset 
│
├── output/
│   └── ocr_results.json         # Final consensus output
│
├── src/
│   ├── ocr_engines/
|   |   ├── base.py
│   │   ├── easyocr_engine.py
│   │   ├── pytesseract_engine.py
│   │   └── trocr_engine.py
│   │
│   ├── utils/
│   │   ├── discrepancy_resolver.py         # Text comparison and selection logic
│   │   └── helpers.py            # To read images from file
│   │
│   └── main.py                  # Entry point
│
├── requirements.txt             # Dependencies
└── README.md
```

## 🚀 Features

- 🔤 **Multi-engine OCR**: Runs EasyOCR, PyTesseract, and TrOCR on each image
- 📊 **Levenshtein-based consensus**: Computes similarity and selects most accurate text
- ✅ **Preserves** punctuation, case, and spacing
- ⚙️ **Logging and error handling** for transparency and debugging
- 🧾 **Structured output** as a JSON file

## 📥 Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ocr-consensus-project.git
cd ocr-consensus-project
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate    # or `.venv\Scripts\activate` on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Install Tesseract OCR binary

For Linux (WSL/Ubuntu):

```bash
sudo apt update
sudo apt install tesseract-ocr
```

Verify installation:

```bash
tesseract --version
```

## 🏃 Run the Project

1. Store the image dataset into the `data/` folder:


2. Run the main script:

```bash
python src/main.py
```

3. Final output: `outputs/ocr_results.json`

## 📊 Output Format

Each entry in `ocr_results.json` is a dictionary:

```json
[
  {
    "image_name": "image_01.jpg",
    "text": "Extracted text from image..."
  }
]
```

## 📈 OCR Evaluation Method

- We compute pairwise **Levenshtein similarity** between outputs from the 3 OCR tools.
- The tool with the **highest average similarity** to the others is chosen as the most accurate.
- Logs track similarity scores and selected engine for transparency.

## 🛠️ Technologies

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [PyTesseract](https://github.com/madmaze/pytesseract)
- [TrOCR (transformers)](https://huggingface.co/microsoft/trocr-base)
- `Levenshtein` for normalized string similarity

## 📝 License

This project is licensed under the MIT License.

## 🙋‍♀️ Contributions

PRs and issues are welcome! Please open a discussion or bug report to contribute.

## 📧 Contact

Feel free to reach out at `prvns1997@gmail.com`.
