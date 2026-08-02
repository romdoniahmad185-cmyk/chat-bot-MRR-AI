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
    # Membaca semua data JSON
    # =====================================

    def load_kosakata(self):

        folder = "data/kosakata"


        if not os.path.exists(folder):

            print("Folder kosakata tidak ditemukan")

            return



        for root, folders, files in os.walk(folder):

            for file in files:


                if file.endswith(".json"):


                    lokasi = os.path.join(root, file)


                    try:

                        with open(
                            lokasi,
                            "r",
                            encoding="utf-8"
                        ) as f:


                            data_json = json.load(f)


                            if isinstance(data_json, list):

                                self.data.extend(data_json)


                            else:

                                print(
                                    "Format JSON salah:",
                                    lokasi
                                )


                            print(
                                "Berhasil membaca:",
                                lokasi
                            )


                    except Exception as error:

                        print(
                            "Gagal membaca:",
                            lokasi
                        )

                        print(error)



        print(
            "Total kosakata:",
            len(self.data)
        )



    # =====================================
    # Menjawab pertanyaan
    # =====================================

    def jawab(self, pertanyaan):


        pertanyaan = pertanyaan.strip().lower()



        if pertanyaan == "":

            return "Silakan masukkan pertanyaan."



        for item in self.data:


            if "tanya" not in item or "jawab" not in item:

                continue



            kata = item["tanya"].lower()



            if kata in pertanyaan:


                return item["jawab"]



        return NOT_FOUND_MESSAGE