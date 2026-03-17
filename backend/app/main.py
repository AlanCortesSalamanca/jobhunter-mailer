from fastapi import FastAPI, UploadFile, File
from app.services.file_parser import extract_emails
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "JobHunter Mailer API running 🚀"}


@app.post("/upload-companies")
async def upload_companies(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    emails = extract_emails(file_location)

    return {
        "total_emails": len(emails),
        "emails": emails[:10]
    }