from fastapi.middleware.cors import CORSMiddleware
from chatbot import Chatbot
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="WEBKITA AI",
    description="API AI Chatbot WEBKITA",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# Inisialisasi Chatbot
# ===============================

bot = Chatbot()
# ===============================
# Model Data dari HTML
# ===============================

class ChatRequest(BaseModel):
    pesan: str

# ===============================
# Halaman Root
# ===============================

@app.get("/")
def home():
    return {
        "status": "online",
        "nama": "WEBKITA AI",
        "versi": "1.0.0"
    }

@app.post("/chat")
def chat(data: ChatRequest):

    pertanyaan = data.pesan

    # Kirim pertanyaan ke Chatbot
    jawaban = bot.jawab(pertanyaan)

    return {
        "status": True,
        "pertanyaan": pertanyaan,
        "jawaban": jawaban
    }