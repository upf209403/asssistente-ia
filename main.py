from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("Assistente iniciado! Digite 'sair' para encerrar.\n")

while True:
    mensagem = input("Você: ")

    if mensagem.lower() == "sair":
        break

    resposta = chat.send_message(mensagem)

    print("\nIA:", resposta.text)
    print()
