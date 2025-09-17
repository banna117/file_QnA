from fastapi import FastAPI
from api import upload, summary

app = FastAPI()
app.include_router(upload.router)
app.include_router(summary.router)