from fastapi import APIRouter
from pydantic import BaseModel
from app.services.vector_db.chroma_client import add_documents

router = APIRouter()

class IngestRequest(BaseModel):
    documents: list[str]

@router.post("/ingest")
async def ingest_data(request: IngestRequest):
    add_documents(request.documents)
    return {"message": "Documents added successfully ✅"}