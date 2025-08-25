from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# inicjalizacja klienta OpenAI z kluczem z environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatIn(BaseModel):
    user_id: str
    message: str

@app.get("/")
def root():
    return {"ok": True, "service": "Master Body Coach Assistant", "version": 1}

@app.post("/chat")
def chat(inp: ChatIn):
    reply = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Jesteś Master Body Coach AI – asystent trenera personalnego."},
            {"role": "user", "content": inp.message}
        ]
    )
    return {"reply": reply.choices[0].message.content}
  
