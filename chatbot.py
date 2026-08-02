"""
=========================================
WEBKITA AI
Chatbot Engine
=========================================
"""

import json
import os

from config import NOT_FOUND_MESSAGE


# =========================================
# Mesin Chatbot
# =========================================

class Chatbot:


    def __init__(self):

        self.data = []

        self.load_kosakata()



    # =====================================
    # Membaca data JSON
    # =====================================

    def load_kosakata(self):

        folder = "data/kosakata"


        if not os.path.exists(folder):
            return


        for file in os.listdir(folder):

            if file.endswith(".json"):

                lokasi = os.path.join(folder,file)


                with open(lokasi,"r",encoding="utf-8") as f:

                    data_json = json.load(f)

                    self.data.extend(data_json)



    # =====================================
    # Menjawab pertanyaan
    # =====================================

    def jawab(self, pertanyaan):

        pertanyaan = pertanyaan.strip().lower()


        if pertanyaan == "":
            return "Silakan masukkan pertanyaan."



        for item in self.data:


            kata = item["tanya"].lower()


            if kata in pertanyaan:

                return item["jawab"]



        return NOT_FOUND_MESSAGE