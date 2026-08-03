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
# Membaca database melalui index.json
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

    # =====================================
    # Gabungkan seluruh daftar file database
    # =====================================

    database_list = []

    database_list.extend(
        index_data.get("percakapan", [])
    )

    database_list.extend(
        index_data.get("kosa-kata", [])
    )

    # =====================================
    # Membaca setiap file JSON
    # =====================================

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

            # Database percakapan
            if (
                isinstance(data_json, dict)
                and "data" in data_json
            ):

                for item in data_json["data"]:

                    if isinstance(item, dict):

                        self.data.append(item)

            # Database kosakata
            elif (
                isinstance(data_json, dict)
                and "kosakata" in data_json
            ):

                for item in data_json["kosakata"]:

                    if isinstance(item, dict):

                        self.data.append(item)

            # Format list langsung
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
    print("Total File     :", self.total_file)
    print("Total Data AI  :", len(self.data))
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


        # =========================
        # Database kosakata
        # =========================

        if "kata" in item:

            kata = item["kata"].lower()


            if kata == kata_dicari:

                skor += 100


            elif kata_dicari in kata:

                skor += 50



        # Cek sinonim

        if "sinonim" in item:

            for sinonim in item["sinonim"]:

                sinonim = sinonim.lower()


                if sinonim == kata_dicari:

                    skor += 80


                elif kata_dicari in sinonim:

                    skor += 40



        # =========================
        # Database percakapan
        # =========================

        if "pertanyaan" in item:

            for pertanyaan in item["pertanyaan"]:

                pertanyaan = pertanyaan.lower()


                if pertanyaan == kata_dicari:

                    skor += 120


                elif kata_dicari in pertanyaan:

                    skor += 60



        return skor

        # =====================================
    # Mencari kata terbaik
    # =====================================

    def cari_kata(self, pertanyaan):

        pertanyaan = pertanyaan.lower().strip()

        hasil = None

        skor_tertinggi = 0


        for item in self.data:

            skor = self.hitung_skor(
                pertanyaan,
                item
            )


            if skor > skor_tertinggi:

                skor_tertinggi = skor

                hasil = item


        return hasil       #=====================================
 # Format jawaban
 # =====================================

    def format_jawaban(self, item):

        jawaban = ""

        # Kata
        if "kata" in item:

            jawaban += f"Kata : {item['kata']}\n\n"

        # Arti
        if "arti" in item:

            jawaban += f"Arti :\n{item['arti']}\n\n"

        # Sinonim
        if "sinonim" in item:

            if len(item["sinonim"]) > 0:

                jawaban += "Sinonim :\n"

                for sinonim in item["sinonim"]:

                    jawaban += f"- {sinonim}\n"

                jawaban += "\n"

        # Contoh
        if "contoh" in item:

            if len(item["contoh"]) > 0:

                jawaban += "Contoh :\n"

                for contoh in item["contoh"]:

                    jawaban += f"- {contoh}\n"

        return jawaban.strip()


    # =====================================
    # Menjawab pertanyaan
    # =====================================

    def jawab(self, pertanyaan):

        pertanyaan = pertanyaan.lower().strip()

        if pertanyaan == "":

            return "Silakan masukkan pertanyaan."


        # ==============================
        # Sapaan
        # ==============================

        sapaan = {

            "hai": "Halo 👋 Ada yang bisa saya bantu?",

            "halo": "Halo 👋 Ada yang bisa saya bantu?",

            "hello": "Halo 👋 Ada yang bisa saya bantu?",

            "assalamualaikum":
                "Waalaikumsalam warahmatullahi wabarakatuh.",

            "selamat pagi":
                "Selamat pagi 😊",

            "selamat siang":
                "Selamat siang 😊",

            "selamat sore":
                "Selamat sore 😊",

            "selamat malam":
                "Selamat malam 😊"

        }


        if pertanyaan in sapaan:

            return sapaan[pertanyaan]


        # ==============================
        # Cari database
        # ==============================

        hasil = self.cari_kata(
            pertanyaan
        )


        if hasil:

            return self.format_jawaban(
                hasil
            )


        return NOT_FOUND_MESSAGE
    # =====================================
    # Menampilkan informasi database
    # =====================================

    def info(self):

        return {
            "total_kosakata": len(self.data),
            "total_file": self.total_file
        }


    # =====================================
    # Reload Database
    # =====================================

    def reload(self):

        self.data = []

        self.total_file = 0

        self.load_database()

        return True


    # =====================================
    # Menambahkan Data Baru
    # =====================================

    def tambah_data(self, data_baru):

        if isinstance(data_baru, dict):

            self.data.append(data_baru)

            return True

        return False


    # =====================================
    # Mengecek apakah kata tersedia
    # =====================================

    def ada_kata(self, kata):

        kata = kata.lower()

        for item in self.data:

            if not isinstance(item, dict):
                continue

            if "kata" not in item:
                continue

            if item["kata"].lower() == kata:

                return True

        return False


    # =====================================
    # Mengambil data kata
    # =====================================

    def ambil_kata(self, kata):

        kata = kata.lower()

        for item in self.data:

            if not isinstance(item, dict):
                continue

            if "kata" not in item:
                continue

            if item["kata"].lower() == kata:

                return item

        return None