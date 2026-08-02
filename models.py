"""
=========================================
WEBKITA AI
Models
=========================================
"""

from pydantic import BaseModel
from typing import Optional

# =========================================
# Request dari Frontend
# =========================================

class ChatRequest(BaseModel):
    pesan: str

# =========================================
# Response ke Frontend
# =========================================

class ChatResponse(BaseModel):
    status: bool
    pertanyaan: str
    jawaban: str

# =========================================
# Data Kosakata
# =========================================

class Kosakata(BaseModel):
    id: str
    kata: str
    jawaban: str

# =========================================
# Informasi AI
# =========================================

class AIInfo(BaseModel):
    nama: str
    versi: str
    author: str

# =========================================
# Error
# =========================================

class ErrorResponse(BaseModel):
    status: bool
    pesan: str