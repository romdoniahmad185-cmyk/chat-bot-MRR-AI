#  """
 # =========================================
 # WEBKITA AI
#  Chatbot Engine
   # =========================================
  #"""

import json
import os

from config import NOT_FOUND_MESSAGE


class Chatbot:

    def __init__(self):
        self.data = []
        self.load_kosakata()

    # =====================================
    # Membaca seluruh file JSON
    # =====================================
    def load_kosakata(self):

        folder = "data/kosa-kata"

        if not os.path.exists(folder):
            print("Folder tidak ditemukan :", folder)
            return

        jumlah_file = 0

        for root, dirs, files in os.walk(folder):

            for file in files:

                if not file.endswith(".json"):
                    continue

                lokasi = os.path.join(root, file)

                try:

                    with open(
                        lokasi,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        data_json = json.load(f)

                        # Format baru
                        if (
                            isinstance(data_json, dict)
                            and "kosakata" in data_json
                        ):

                            self.data.extend(
                                data_json["kosakata"]
                            )

                        # Format lama
                        elif isinstance(data_json, list):

                            self.data.extend(data_json)

                        jumlah_file += 1

                        print("Berhasil :", lokasi)

                except Exception as e:

                    print("Gagal :", lokasi)
                    print(e)

        print("--------------------------------")
        print("Total File :", jumlah_file)
        print("Total Kosakata :", len(self.data))
        print("--------------------------------")

    # =====================================
    # Hitung skor kecocokan
    # =====================================
    def hitung_skor(self, pertanyaan, kata):

        skor = 0

        pertanyaan = pertanyaan.lower()

        for k in kata.lower().split():

            if k in pertanyaan:
                skor += 1

        return skor

    # =====================================
    # Menjawab pertanyaan
    # =====================================
    def jawab(self, pertanyaan):

        pertanyaan = pertanyaan.lower().strip()

        if pertanyaan == "":
            return "Silakan masukkan pertanyaan."

        skor_tertinggi = 0
        hasil = None

        for item in self.data:

            if not isinstance(item, dict):
                continue

            if "kata" not in item:
                continue

            skor = self.hitung_skor(
                pertanyaan,
                item["kata"]
            )

            # cek sinonim
            if "sinonim" in item:

                for sinonim in item["sinonim"]:

                    skor += self.hitung_skor(
                        pertanyaan,
                        sinonim
                    )

            if skor > skor_tertinggi:

                skor_tertinggi = skor

                hasil = item

        if hasil:

            jawaban = ""

            jawaban += f"Kata : {hasil['kata']}\n\n"

            if "arti" in hasil:
                jawaban += f"Arti :\n{hasil['arti']}\n\n"

            if (
                "contoh" in hasil
                and len(hasil["contoh"]) > 0
            ):

                jawaban += "Contoh:\n"

                for contoh in hasil["contoh"]:

                    jawaban += f"- {contoh}\n"

            return jawaban.strip()

        return NOT_FOUND_MESSAGE