from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

app = FastAPI()


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    
    response = {
        "filename": file.filename,
        "format": image.format,
        "width": image.width,
        "height": image.height
    }
    
    print(response)
    return response

