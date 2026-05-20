from fastapi import FastAPI
from routes.chat import router as chat_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "A API está funcionando"}

app.include_router(chat_router, prefix="/chat")