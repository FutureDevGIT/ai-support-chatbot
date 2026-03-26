from app.services.rag.embeddings import embed_text
from app.services.vector_db.chroma_client import query_documents

async def retrieve_context(query: str):
    embedding = embed_text(query)
    docs = query_documents(embedding)

    return "\n".join(docs)