from google import genai
from dotenv import load_dotenv
import os

from utils.detect_topic import detect_topic
from utils.load_knowledge import load_knowledge

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

def load_chat_prompt():
    with open("../prompts/chat.txt", "r", encoding="utf-8") as f:
        return f.read()

def ask_gemini(user_prompt: str):

    chat_prompt = load_chat_prompt()

    topics = detect_topic(user_prompt)

    if(type(topics) == str): return topics

    knowledge = load_knowledge(topics)

    final_prompt = f"""
        INSTRUÇÕES DO ASSISTENTE:
        {chat_prompt}
        
        CONHECIMENTO RELEVANTE:
        {knowledge}

        PERGUNTA DO USUÁRIO:
        {user_prompt}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    return response.text