"""
=========================================
WEBKITA AI
Chatbot Engine
=========================================
"""

from config import NOT_FOUND_MESSAGE

# =========================================
# Mesin Chatbot
# =========================================

class Chatbot:

    def __init__(self):
        pass

    def jawab(self, pertanyaan):

        pertanyaan = pertanyaan.strip()

        if pertanyaan == "":
            return "Silakan masukkan pertanyaan."

        # sementara
        return NOT_FOUND_MESSAGE