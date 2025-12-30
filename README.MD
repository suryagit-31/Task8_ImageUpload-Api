# FastAPI Image Upload API

A minimal FastAPI application that accepts an image upload and returns its format and dimensions.

---


## Clone the Repository

```bash
git clone https://github.com/suryagit-31/Task8_ImageUpload-Api.git
cd Task8_ImageUpload-Api


### 1. Create and activate virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows


## Setup & Run (Local)
│── main.py
│── requirements.txt
│── .gitignore
│── myenv/


2.  Install Dependencies 

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