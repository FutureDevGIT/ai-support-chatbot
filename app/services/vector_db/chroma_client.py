import uuid

_documents = []

def add_documents(docs):
    for doc in docs:
        _documents.append({"id": str(uuid.uuid4()), "text": doc})

def query_documents(query_text: str, top_k=3):
    query_words = set(query_text.lower().split())
    
    scored = []
    for doc in _documents:
        doc_words = set(doc["text"].lower().split())
        score = len(query_words & doc_words)
        scored.append((score, doc["text"]))
    
    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]

_default_docs = [
    "To reset password, go to settings and click 'Forgot Password'.",
    "You can contact support at support@example.com.",
    "Refunds are processed within 5-7 business days."
]
add_documents(_default_docs)
