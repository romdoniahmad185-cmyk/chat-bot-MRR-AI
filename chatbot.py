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