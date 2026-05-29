from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv
import os

from utils.detect_topic import detect_topic
from utils.load_knowledge import load_knowledge

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

from pathlib import Path

BASE_DIR_CHAT = Path(__file__).resolve().parent.parent

def load_chat_prompt():

    chat_prompt_path = BASE_DIR_CHAT/ "prompts"/ "chat.txt"
    with open(chat_prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def ask_gemini(user_prompt: str):

    topics = detect_topic(user_prompt)

    if(type(topics) == str): return topics

    chat_prompt = load_chat_prompt()

    knowledge = load_knowledge(topics)

    print("\n===== TOPICS =====")
    print(topics)

    print("\n===== KNOWLEDGE SIZE =====")
    print(len(knowledge))

    print("\n===== KNOWLEDGE PREVIEW =====")
    print(knowledge[:500])

    print("\n===== CHAT PROMPT PREVIEW =====")
    print(chat_prompt[:500])

    final_prompt = f"""
        INSTRUÇÕES DO ASSISTENTE:
        {chat_prompt}
        
        CONHECIMENTO RELEVANTE:
        {knowledge}

        PERGUNTA DO USUÁRIO:
        {user_prompt}
    """

    print("\n===== FINAL PROMPT SIZE =====")
    print(len(final_prompt))

    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

        return response.text
    
    except ServerError as e:
        print(e)

        return {
            "error": True,
            "message": "Serviço temporariamente indisponível"
        }
