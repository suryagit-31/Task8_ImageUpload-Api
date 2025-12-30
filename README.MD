# FastAPI Image Upload API

A minimal FastAPI application that accepts an image file and returns its format and dimensions as JSON.

---

## Project Structure
Task8_ImageUpload-Api/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore

yaml
Copy code

---

### Clone the Repository

```bash
git clone https://github.com/suryagit-31/Task8_ImageUpload-Api.git
cd Task8_ImageUpload-Api

1.Setup & Run Locally
1. Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate   # Windows



2. Install dependencies
pip install -r requirements.txt


3. Run the FastAPI server
bash
Copy code
uvicorn main:app --reload

Server runs at: http://127.0.0.1:8000



4.API Endpoint

POST /upload-image
Accepts an image file

Processes the image in memory

Returns image metadata as JSON

Sample Response
json
{
  "filename": "image.png",
  "format": "PNG",
  "width": 640,
  "height": 480
}


5. Testing
Swagger UI (Recommended)
Open:
arduino
Copy code
http://127.0.0.1:8000/docs


Curl (Terminal)
bash
Copy code
curl -X POST http://127.0.0.1:8000/upload-image \
     -F "file=@image.png"
Notes
Images are processed in memory and not saved to disk

Virtual environment is excluded from GitHub

Tech Stack
Python

FastAPI

Uvicorn

Pillow