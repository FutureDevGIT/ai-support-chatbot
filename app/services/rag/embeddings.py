from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def embed_text(text: str):
    return text
