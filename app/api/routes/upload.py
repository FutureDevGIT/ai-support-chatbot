from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.file.parser import extract_text_from_pdf, extract_text_from_txt
from app.services.rag.chunker import chunk_text
from app.services.vector_db.chroma_client import add_documents

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file.filename.endswith(".txt"):
        text = extract_text_from_txt(file_path)
    else:
        return {"error": "Unsupported file type"}

    # Chunking
    chunks = chunk_text(text)

    # Store in vector DB
    add_documents(chunks)

    return {
        "message": "File uploaded and processed ✅",
        "chunks_created": len(chunks)
    }