# OCR-api

Foobar is a REST API for accessing OCR(Optical character recognition). It is written in Python FastAPI framework. OCR API is based on Tesseract[https://github.com/tesseract-ocr/tesseract], an open source OCR engine currently maintained by Google.

You can upload images of english characters to this API, and access the corresponding string in JSON format.


## Installation

You would need to install Tesseract, and Pytesseract which is a python wrapper for Tesseract on your system.

- Ubuntu – For Ubuntu users, you can use the following command:
```bash
sudo apt-get install tesseract-ocr
```
- Windows – For Windows users, you can visit [https://github.com/UB-Mannheim/tesseract/wiki] and select 32-bit/64-bit as per your system.
- Mac – For macOS users, you can use Homebrew to install Tesseract. The command is shown below:
```bash
brew install tesseract
```

Use Python Virtual Environment.
To install: 
```bash
pip install venv
```
To create virtual environment:
```bash
python -m venv path\[env_name]
```
To activate virtual environment:
```bash
source path\[env_name]\bin\activate
```
To install required packages:
```bash
python install -r requirement.txt
```


## Usage

To run the server:
```bash
run server: uvicorn main:app --reload
```

