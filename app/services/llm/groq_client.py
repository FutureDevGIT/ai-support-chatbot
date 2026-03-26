import httpx
import os
from app.services.llm.base import BaseLLM
from app.core.config import settings

GROQ_API_KEY = settings.GROQ_API_KEY

class GroqClient(BaseLLM):
    async def generate(self, query: str, context: str = "") -> str:
        prompt = f"""
        You are a helpful support assistant.

        Context:
        {context}

        User Query:
        {query}
        """

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.1-8b-instant",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3
                }
            )

        data = response.json()

        if "error" in data:
            raise Exception(data["error"]["message"])

        return data["choices"][0]["message"]["content"]