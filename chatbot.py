def jawab(self, pertanyaan):

    pertanyaan = pertanyaan.lower().strip()

    if not pertanyaan:
        return "Silakan masukkan pertanyaan."

    skor_tertinggi = 0
    jawaban = None

    for item in self.data:

        if "tanya" not in item or "jawab" not in item:
            continue

        kata = item["tanya"].lower()

        skor = 0

        for k in kata.split():
            if k in pertanyaan:
                skor += 1

        if skor > skor_tertinggi:
            skor_tertinggi = skor
            jawaban = item["jawab"]

    if jawaban:
        return jawaban

    return NOT_FOUND_MESSAGE