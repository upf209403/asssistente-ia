from fastapi import APIRouter
from pydantic import BaseModel

from services.chatService import ask_gemini

router = APIRouter()

class Message(BaseModel):
    prompt: str

@router.post("/")
def chat(message: Message):
    response = ask_gemini(message.prompt)

    return {
        "response": response
    }