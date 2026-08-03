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

        self.load_database()
    # =====================================
    # Membaca seluruh database
    # =====================================

    def load_database(self):

        index_file = "index.json"

        if not os.path.exists(index_file):

            print("Index database tidak ditemukan :", index_file)

            return


        print("================================")
        print("Memuat database WEBKITA AI...")
        print("================================")


        try:

            with open(
                index_file,
                "r",
                encoding="utf-8"
            ) as f:

                index_data = json.load(f)

        except Exception as error:

            print("Gagal membaca index.json")

            print(error)

            return


        # Gabungkan semua file database

        database_list = []

        database_list.extend(
            index_data.get("percakapan", [])
        )

        database_list.extend(
            index_data.get("kosa-kata", [])
        )


        for lokasi in database_list:

            if not os.path.exists(lokasi):

                print("File tidak ditemukan :", lokasi)

                continue


            try:

                with open(
                    lokasi,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data_json = json.load(f)


                # Database Percakapan

                if (
                    isinstance(data_json, dict)
                    and "data" in data_json
                ):

                    for item in data_json["data"]:

                        if isinstance(item, dict):

                            self.data.append(item)


                # Database Kosakata

                elif (
                    isinstance(data_json, dict)
                    and "kosakata" in data_json
                ):

                    for item in data_json["kosakata"]:

                        if isinstance(item, dict):

                            self.data.append(item)


                self.total_file += 1

                print("Berhasil :", lokasi)


            except Exception as error:

                print("Gagal :", lokasi)

                print(error)


        print("================================")
        print("Total File :", self.total_file)
        print("Total Data :", len(self.data))
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

        # Database Kosakata
        if "kata" in item:

            kata = item["kata"].lower()

            if kata == kata_dicari:

                skor += 100

            elif kata_dicari in kata:

                skor += 50


        if "sinonim" in item:

            for sinonim in item["sinonim"]:

                sinonim = sinonim.lower()

                if sinonim == kata_dicari:

                    skor += 80

                elif kata_dicari in sinonim:

                    skor += 40


        # Database Percakapan
        if "pertanyaan" in item:

            for pertanyaan in item["pertanyaan"]:

                pertanyaan = pertanyaan.lower()

                if pertanyaan == kata_dicari:

                    skor += 120

                elif kata_dicari in pertanyaan:

                    skor += 60

        return skor


    # =====================================
    # Mencari data terbaik
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
    # =====================================
    # Format Jawaban
    # =====================================

    def format_jawaban(self, item):

        # =========================
        # Database Percakapan
        # =========================

        if "jawaban" in item:

            if len(item["jawaban"]) > 0:

                return item["jawaban"][0]

        # =========================
        # Database Kosakata
        # =========================

        jawaban = ""

        if "kata" in item:

            jawaban += f"Kata : {item['kata']}\n\n"


        if "arti" in item:

            jawaban += f"Arti :\n{item['arti']}\n\n"


        if "sinonim" in item:

            if len(item["sinonim"]) > 0:

                jawaban += "Sinonim :\n"

                for sinonim in item["sinonim"]:

                    jawaban += f"- {sinonim}\n"

                jawaban += "\n"


        if "contoh" in item:

            if len(item["contoh"]) > 0:

                jawaban += "Contoh :\n"

                for contoh in item["contoh"]:

                    jawaban += f"- {contoh}\n"

        return jawaban.strip()


    # =====================================
    # Menjawab Pertanyaan
    # =====================================

    def jawab(self, pertanyaan):

        pertanyaan = pertanyaan.lower().strip()

        if pertanyaan == "":

            return "Silakan masukkan pertanyaan."


        hasil = self.cari_kata(
            pertanyaan
        )


        if hasil:

            return self.format_jawaban(
                hasil
            )


        return NOT_FOUND_MESSAGE