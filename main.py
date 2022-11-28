from fastapi import FastAPI, UploadFile, File
from typing import List
import asyncio
import time
import utils
import ocr


app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []
    for img in Images:
        print("Image uploaded:", img.filename)
        temp_file = utils._save_file_to_server(img, path = "./", save_as = img.filename)
        tasks.append(asyncio.create_task(ocr.read_image(temp_file)))
    texts = asyncio.gather(*tasks)
    for i, text in enumerate(texts):
        response[Images[i].filename] = text
    response["Time Taken"] = round(time.time() - s, 2)
    return response