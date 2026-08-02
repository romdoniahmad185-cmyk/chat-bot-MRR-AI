from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="WEBKITA AI",
    description="API AI Chatbot WEBKITA",
    version="1.0.0"
)

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

# ===============================
# Endpoint Chat
# ===============================

@app.post("/chat")
def chat(data: ChatRequest):

    pertanyaan = data.pesan

    # sementara jawaban sederhana
    jawaban = f"Anda bertanya : {pertanyaan}"

    return {
        "status": True,
        "pertanyaan": pertanyaan,
        "jawaban": jawaban
    }