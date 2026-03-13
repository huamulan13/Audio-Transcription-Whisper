import requests
import json
import os
from dotenv import load_dotenv

load_dotenv("../.env")

API_KEY = os.getenv("API_KEY")
API_WISPER_URL = os.getenv("WHISPER_URL")

url = f"{API_WISPER_URL}/v1/audio/transcriptions"
file_path = "wave to earth - bad (cover).mp3"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "model": "whisper-large-v3",
    "language": "english",
    "response_format": "json"
}

print(f"Sedang memproses audio (via .env config)...")

try:
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f, 'audio/mpeg')}
        response = requests.post(url, files=files, data=data, headers=headers)
    
    response.raise_for_status()
    result = response.json()

    if 'transcript' in result:
        transcription = result['transcript']['text']
        print("\n--- HASIL TRANSKRIPSI ---")
        print(transcription.strip())
    else:
        print("Gagal mengambil teks, cek struktur JSON.")

except Exception as e:
    print(f"Waduh, ada error: {e}")