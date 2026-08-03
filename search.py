#"""
#=========================================
#WEBKITA AI
#Search Engine
#=========================================
#"""

class Search:

    def __init__(self):
        pass

    # =====================================
    # Cari berdasarkan kata
    # =====================================

    def find(self, keyword, data):

        keyword = keyword.lower().strip()

        for item in data:

            kata = item.get("kata", "").lower()

            if keyword == kata:

                return item

        return None

    # =====================================
    # Cari berdasarkan sebagian kata
    # =====================================

    def find_contains(self, keyword, data):

        keyword = keyword.lower().strip()

        hasil = []

        for item in data:

            kata = item.get("kata", "").lower()

            if keyword in kata:

                hasil.append(item)

        return hasil

    # =====================================
    # Hitung jumlah data
    # =====================================

    def total(self, data):

        return len(data)