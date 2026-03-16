from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "JobHunter Mailer API running"}
    