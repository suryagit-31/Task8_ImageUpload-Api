# FastAPI Image Upload API

A minimal FastAPI application that accepts an image upload and returns its format and dimensions.

---

## Setup & Run (Local)
│── main.py
│── requirements.txt
│── .gitignore
│── myenv/


### 1. Create and activate virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows


2. After Cloning and Activation of enviorment 
pip install -r requirements.txt

##
pip install fastapi uvicorn pillow python-multipart

3. Run the server
uvicorn main:app --reload


Server will start at: http://127.0.0.1:8000

API Endpoint
POST /upload-image

Accepts an image file

Returns image metadata as JSON

Sample Response
{
  "filename": "image.png",
  "format": "PNG",
  "width": 640,
  "height": 480
}

Testing

Open Swagger UI:

http://127.0.0.1:8000/docs


Upload an image and view the response.

Tech Stack

Python

FastAPI

Uvicorn

Pillow