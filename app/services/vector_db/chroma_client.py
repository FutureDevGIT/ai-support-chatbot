import chromadb
import uuid

client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="./chroma_db"
    )
)

collection = client.get_or_create_collection(name="support_docs")

def add_documents(docs):
    for doc in docs:
        collection.add(
            documents=[doc],
            ids=[str(uuid.uuid4())]
        )

def query_documents(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]

docs = [
    "To reset password, go to settings and click 'Forgot Password'.",
    "You can contact support at support@example.com.",
    "Refunds are processed within 5-7 business days."
]

add_documents(docs)