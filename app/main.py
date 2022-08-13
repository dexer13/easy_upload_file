import shutil
from typing import Union

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}
