from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

app = FastAPI() #Create a FastAPI instance

@app.post("/upload-image")
#Function to handle image upload and return its properties
async def upload_image(file: UploadFile = File(...)):
    image_bytes = await file.read() #Read the uploaded file bytes
    image = Image.open(io.BytesIO(image_bytes)) #Open the image from the uploaded file bytes
    
    response = {
        "filename": file.filename,
        "format": image.format,
        "width": image.width,
        "height": image.height
    }
    
    print(response) #Log the response to the console
    return response

