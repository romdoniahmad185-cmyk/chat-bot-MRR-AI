"""
=========================================
WEBKITA AI
Chatbot Engine
=========================================
"""

import json
import os

from config import NOT_FOUND_MESSAGE


class Chatbot:

    def __init__(self):
        self.data = []
        self.load_kosakata()

    # =====================================
    # Membaca semua file JSON
    # =====================================
    def load_kosakata(self):

        folder = "data/kosakata"

        if not os.path.exists(folder):
            print("Folder tidak ditemukan :", folder)
            return

        jumlah_file = 0

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.endswith(".json"):

                    lokasi = os.path.join(root, file)

                    try:

                        with open(
                            lokasi,
                            "r",
                            encoding="utf-8"
                        ) as f:

                            data = json.load(f)

                            if isinstance(data, list):
                                self.data.extend(data)
                            elif isinstance(data, dict):
                                self.data.append(data)

                            jumlah_file += 1

                            print("Berhasil :", lokasi)

                    except Exception as e:
                        print("Gagal :", lokasi)
                        print(e)

        print("--------------------------------")
        print("Total File :", jumlah_file)
        print("Total Data :", len(self.data))
        print("--------------------------------")

    # =====================================
    # Menghitung kecocokan kata
    # =====================================
    def hitung_skor(self, pertanyaan, kalimat):

        skor = 0

        kata_database = kalimat.lower().split()

        for kata in kata_database:

            if kata in pertanyaan:
                skor += 1

        return skor

    # =====================================
    # Menjawab Pertanyaan
    # =====================================
    def jawab(self, pertanyaan):

        pertanyaan = pertanyaan.lower().strip()

        if pertanyaan == "":
            return "Silakan masukkan pertanyaan."

        skor_tertinggi = 0
        jawaban_terbaik = None

        for item in self.data:

            if not isinstance(item, dict):
                continue

            if "tanya" not in item:
                continue

            if "jawab" not in item:
                continue

            skor = self.hitung_skor(
                pertanyaan,
                item["tanya"]
            )

            if skor > skor_tertinggi:

                skor_tertinggi = skor
                jawaban_terbaik = item["jawab"]

        if jawaban_terbaik:
            return jawaban_terbaik

        return NOT_FOUND_MESSAGE