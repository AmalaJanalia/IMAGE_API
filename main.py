from fastapi import FastAPI
from util import get_image_as_binary, convert_to_base64
app = FastAPI()

@app.get("/image64")
def getimageb64(path):
    image_binary = get_image_as_binary(path)
    image_base_64 = convert_to_base64(image_binary)

    return {
        "statuscode" : 200,
        "content" : image_base_64 

    }
