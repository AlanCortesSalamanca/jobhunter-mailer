from fastapi import FastAPI, UploadFile, File, Form
from app.services.file_parser import extract_emails
import shutil
from app.services.email_sender import send_emails
from app.services.logger import log_queue
from app.services.file_parser import extract_companies_from_excel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import asyncio
from fastapi import BackgroundTasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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




@app.post("/send-emails")
async def send_emails_endpoint(
    background_tasks: BackgroundTasks,
    sender_email: str = Form(...),
    sender_password: str = Form(...),
    subject: str = Form(...),
    body: str = Form(...),
    excel: UploadFile = File(...),
    cv: UploadFile = File(...)
):

    # Guardar archivos temporalmente
    excel_path = f"temp_{excel.filename}"
    cv_path = f"temp_{cv.filename}"

    with open(excel_path, "wb") as f:
        f.write(await excel.read())

    with open(cv_path, "wb") as f:
        f.write(await cv.read())

    companies = extract_companies_from_excel(excel_path)

    background_tasks.add_task(
        send_emails,
        sender_email,
        sender_password,
        companies,
        subject,
        body,
        cv_path
    )

    return {"message": "Envío iniciado 🚀"}
    


async def log_generator():
    while True:
        if log_queue:
            message = log_queue.pop(0)
            yield f"data: {message}\n\n"
        await asyncio.sleep(0.1)

@app.get("/logs")
async def get_logs():
    return StreamingResponse(log_generator(), media_type="text/event-stream")