import os
from dotenv import load_dotenv

# Coba load
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print("--- DIAGNOSA KUNCI ---")
if api_key:
    print("✅ Kunci DITEMUKAN!")
    print(f"Depan: {api_key[:5]}...")
    print(f"Belakang: ...{api_key[-5:]}")
else:
    print("❌ Kunci TIDAK ditemukan.")
    print("Pastikan file bernama '.env' (bukan .env.txt)")
    print("Pastikan file '.env' ada di folder yang sama dengan script ini.")