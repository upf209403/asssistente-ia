from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import os

load_dotenv()

app = FastAPI()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-2.5-flash"
)

class Message(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "A API está funcionando"}

@app.post("/chat")
def conversar(message: Message):

    resposta = chat.send_message(message.prompt)

    return { 
        "response": resposta.text
    }
