from app.services.llm.groq_client import GroqClient

def get_llm(provider: str):
    if provider == "groq":
        return GroqClient()
    else:
        raise ValueError(f"Unsupported provider: {provider}")