#"""
#=========================================
#WEBKITA AI
#Chatbot Engine
#=========================================
#"""

import json
import os

from config import NOT_FOUND_MESSAGE


class Chatbot:

    def __init__(self):

        self.data = []

        self.total_file = 0

        self.load_kosakata()


    # =====================================
    # Membaca seluruh file JSON
    # =====================================

    def load_kosakata(self):

        folder = "data/kosa-kata"

        if not os.path.exists(folder):

            print("Folder tidak ditemukan :", folder)

            return


        print("================================")
        print("Memuat database WEBKITA AI...")
        print("================================")


        for root, dirs, files in os.walk(folder):

            files.sort()

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


                        # Format database baru
                        if (
                            isinstance(data_json, dict)
                            and "kosakata" in data_json
                        ):

                            for item in data_json["kosakata"]:

                                if isinstance(item, dict):

                                    self.data.append(item)


                        # Format lama
                        elif isinstance(data_json, list):

                            for item in data_json:

                                if isinstance(item, dict):

                                    self.data.append(item)


                        self.total_file += 1

                        print("Berhasil :", lokasi)

                except Exception as error:

                    print("Gagal :", lokasi)

                    print(error)


        print("================================")
        print("Total File      :", self.total_file)
        print("Total Kosakata  :", len(self.data))
        print("================================")
    # =====================================
    # Membersihkan pertanyaan
    # =====================================

    def bersihkan_pertanyaan(self, pertanyaan):

        stopword = {
            "apa",
            "itu",
            "arti",
            "dari",
            "yang",
            "dan",
            "atau",
            "adalah",
            "jelaskan",
            "definisi",
            "maksud",
            "tentang",
            "tolong",
            "mohon",
            "kah",
            "nya"
        }

        hasil = []

        for kata in pertanyaan.lower().split():

            if kata not in stopword:

                hasil.append(kata)

        return hasil


    # =====================================
    # Menghitung skor kecocokan
    # =====================================

    def hitung_skor(self, kata_dicari, item):

        skor = 0

        # Cek kata utama
        if "kata" in item:

            if item["kata"].lower() == kata_dicari:

                skor += 100

            elif kata_dicari in item["kata"].lower():

                skor += 50


        # Cek sinonim
        if "sinonim" in item:

            for sinonim in item["sinonim"]:

                sinonim = sinonim.lower()

                if sinonim == kata_dicari:

                    skor += 80

                elif kata_dicari in sinonim:

                    skor += 40

        return skor


    # =====================================
    # Mencari kata terbaik
    # =====================================

    def cari_kata(self, pertanyaan):

        kata_dicari = self.bersihkan_pertanyaan(
            pertanyaan
        )

        hasil = None

        skor_tertinggi = 0

        for kata in kata_dicari:

            for item in self.data:

                skor = self.hitung_skor(
                    kata,
                    item
                )

                if skor > skor_tertinggi:

                    skor_tertinggi = skor

                    hasil = item

        return hasil