"""
=========================================
WEBKITA AI
Loader Data
=========================================
"""

import json
import requests

from config import GITHUB_RAW

# =========================================
# Loader
# =========================================

class Loader:

    def __init__(self):
        self.data = []

    # =====================================
    # Membaca JSON dari Github
    # =====================================

    def load_json(self, path):

        url = GITHUB_RAW + path

        try:

            response = requests.get(url, timeout=10)

            if response.status_code == 200:

                return response.json()

            return None

        except Exception as e:

            print("Loader Error :", e)

            return None

    # =====================================
    # Menyimpan Data
    # =====================================

    def add(self, item):

        self.data.append(item)

    # =====================================
    # Mengambil Semua Data
    # =====================================

    def get_all(self):

        return self.data

    # =====================================
    # Menghapus Data
    # =====================================

    def clear(self):

        self.data.clear()