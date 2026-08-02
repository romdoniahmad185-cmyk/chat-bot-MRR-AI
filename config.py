"""
=========================================
WEBKITA AI
File Konfigurasi
=========================================
"""

# =====================================================
# IDENTITAS AI
# =====================================================

AI_NAME = "WEBKITA AI"

AI_VERSION = "1.0.0"

AI_AUTHOR = "WEBKITA"

AI_LANGUAGE = "id"

# =====================================================
# GITHUB
# =====================================================

# Username Github
GITHUB_USERNAME = "romdoniahmad185-cmyk"

# Repository Github
GITHUB_REPOSITORY = "chatbot"

# Branch
GITHUB_BRANCH = "main"

# URL Raw Github
GITHUB_RAW = (
    f"https://raw.githubusercontent.com/"
    f"{GITHUB_USERNAME}/"
    f"{GITHUB_REPOSITORY}/"
    f"{GITHUB_BRANCH}/"
)

# =====================================================
# FOLDER DATA
# =====================================================

DATA_FOLDER = "data"

KOSAKATA_FOLDER = "data/kosakata"

# =====================================================
# CHATBOT
# =====================================================

MAX_CHAT_LENGTH = 500

MAX_HISTORY = 20

NOT_FOUND_MESSAGE = (
    "Maaf, saya belum menemukan jawaban "
    "untuk pertanyaan tersebut."
)

# =====================================================
# API
# =====================================================

API_HOST = "0.0.0.0"

API_PORT = 8000

# =====================================================
# DEBUG
# =====================================================

DEBUG = True