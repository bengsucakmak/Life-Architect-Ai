# config.py

import os
from dotenv import load_dotenv, find_dotenv

# Proje kökündeki .env dosyasını bulup yükle
load_dotenv(find_dotenv())

# Debug amaçlı: terminalde hangi değerlerin geldiğini görebilirsin
print("🔧 DEBUG – Config Yükleniyor:")
print("API_KEY       =", os.getenv("API_KEY"))
print("BASE_URL      =", os.getenv("BASE_URL"))
print("MODEL_NAME    =", os.getenv("MODEL_NAME"))
print("VOICE_ENABLED =", os.getenv("VOICE_ENABLED"))

# Asıl kullanacağımız değişkenler
API_KEY     = os.getenv("API_KEY")
BASE_URL    = os.getenv("BASE_URL", "https://api.intelligence.io.solutions/api/v1")
MODEL_NAME  = os.getenv("MODEL_NAME", "meta-llama/Llama-3.3-70B-Instruct")
# VOICE_ENABLED için True/False kararı
VOICE_ENABLED = os.getenv("VOICE_ENABLED", "True").strip().lower() in ("1", "true", "yes")
