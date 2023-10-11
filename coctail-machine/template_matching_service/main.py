from fastapi import FastAPI, Form, UploadFile
import uvicorn
import base64
from cropBottles import cropBottles

app = FastAPI()

# @app.post("/bottles/cropBottles")
# def getBottles(file: UploadFile):
#     contents = file.file.read()
#     try:
#         with open("./images/imageToSave.png", "wb") as fh:
#             fh.write(base64.b64decode(contents))
#     except Exception:
#         return {"message": "There was an error uploading the file"}


@app.post("/bottles/cropBottles")
def getBottles(imagebase64: str = Form(...)):
    image_as_bytes = str.encode(imagebase64)
    image = base64.b64decode(image_as_bytes)
    with open("./images/bottles.png", "wb") as fh:
        fh.write(image)
    return cropBottles("./images/bottles.png")

@app.post("/bottles/fillLevel")
def upload(image: str = Form(...)):
    image_as_bytes = str.encode(image)
    img_recovered = base64.b64decode(image_as_bytes)
    try:
        with open("martini", "wb") as fh:
            fh.write(img_recovered)
    except Exception:
        return {"message": "There was an error uploading the file"}

    return {"message": "Successfuly uploaded {filename}"}

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, log_level="info")