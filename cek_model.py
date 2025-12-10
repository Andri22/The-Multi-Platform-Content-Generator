import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- DAFTAR MODEL YANG TERSEDIA ---")
try:
    for m in genai.list_models():
        # Kita hanya cari model yang bisa generate text (bukan image/embedding)
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ {m.name}")
except Exception as e:
    print(f"Error saat cek model: {e}")