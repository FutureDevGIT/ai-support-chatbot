from app.services.rag.embeddings import embed_text
from app.services.vector_db.chroma_client import query_documents

async def retrieve_context(query: str):
    query_text = embed_text(query)
    docs = query_documents(query_text)
    return "\n".join(docs)
