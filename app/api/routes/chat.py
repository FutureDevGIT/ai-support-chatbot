from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm.factory import get_llm
from app.services.rag.retriever import retrieve_context
from app.services.memory.store import add_message, get_history

router = APIRouter()


def format_history(history):
    formatted = ""

    for msg in history:
        if msg["role"] == "user":
            formatted += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            formatted += f"Assistant: {msg['content']}\n"

    return formatted


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    llm = get_llm(request.provider)

    # ✅ Limit history (important)
    history = get_history(request.user_id)[-5:]

    # ✅ Format history properly
    formatted_history = format_history(history)

    # Get RAG context
    search_query = request.query

    if history:
        last_user_msg = history[-1]["content"]
        search_query = last_user_msg + " " + request.query

    context = await retrieve_context(search_query)

    # ✅ Clean prompt
    full_prompt = f"""
You are a highly accurate AI support assistant.

STRICT RULES:
1. Always use the provided CONTEXT to answer.
2. If CONTEXT contains the answer, DO NOT use outside knowledge.
3. Use conversation history only to understand references like "it", "that", etc.
4. If answer is not in context, say: "I don't have that information."

Conversation History:
{formatted_history}

Context:
{context}

User: {request.query}

Answer clearly and concisely:
"""

    answer = await llm.generate(
        query=full_prompt,
        context=""
    )

    # Save conversation
    add_message(request.user_id, "user", request.query)
    add_message(request.user_id, "assistant", answer)

    return ChatResponse(
        answer=answer.strip(),
        source="memory+rag"
    )