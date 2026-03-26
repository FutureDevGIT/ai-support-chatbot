# In-memory store (for now)
chat_memory = {}

def get_history(user_id: str):
    return chat_memory.get(user_id, [])

def add_message(user_id: str, role: str, content: str):
    if user_id not in chat_memory:
        chat_memory[user_id] = []

    chat_memory[user_id].append({
        "role": role,
        "content": content
    })