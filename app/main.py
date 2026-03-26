from fastapi import FastAPI
from app.api.routes import chat, ingest, upload

app = FastAPI(
    title="AI Support Chatbot API",
    version="1.0.0"
)

app.include_router(chat.router, prefix="/api")
app.include_router(ingest.router, prefix="/api")
app.include_router(upload.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API is running 🚀"}