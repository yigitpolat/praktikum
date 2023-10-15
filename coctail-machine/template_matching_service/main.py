from fastapi import FastAPI, Form, UploadFile
import uvicorn
import base64
from cropBottles import cropBottles
from liquid_level import is_bottle_full

app = FastAPI()

@app.post("/bottles/cropBottles")
def getBottles(imagebase64: str = Form(...)):
    imagebase64 = str(imagebase64).split(';')[1]
    image_as_bytes = str.encode(imagebase64)
    image = base64.b64decode(image_as_bytes)
    try:
        with open("./images/bottles.png", "wb") as fh:
            fh.write(image)
        return cropBottles("./images/bottles.png")
    except Exception as e:
        return {"error": e}

@app.post("/bottles/fillLevel")
def upload(imagebase64: str = Form(...)):
    imagebase64 = str(imagebase64).split(';')[1]
    image_as_bytes = str.encode(imagebase64)
    image = base64.b64decode(image_as_bytes)
    try:
        with open("./images/bottle.png", "wb") as fh:
            fh.write(image)
        return is_bottle_full("./images/bottle.png")
    except Exception as e:
        return {"error": e}

if __name__ == '__main__':
   uvicorn.run("main:app", host="::", port=8011, log_level="info")