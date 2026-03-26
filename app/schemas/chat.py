from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    query: str = Field(..., min_length=1)
    user_id: str
    provider: str = "groq"  # future use

class ChatResponse(BaseModel):
    answer: str
    source: str | None = None