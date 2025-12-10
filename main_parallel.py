import os
import asyncio
import time
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from groq import AsyncGroq
# from openai import AsyncOpenAI # <--- Import beda

# --- 1. CONFIG & SETUP STREAMLIT---
st.set_page_config(page_title="AI Content Generator", layout="wide") # Biar lebar

# 1. Load Environment 
load_dotenv()
# Gemini
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Setup Client
client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY")
)
#OpenAI
# client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 2. System Instruction (Otak/Kepribadian AI)
SYSTEM_PROMPT = """
Kamu adalah Expert Social Media Strategist. 
Gaya bahasa kamu menarik, viral, tapi tetap profesional.
Selalu gunakan Bahasa Indonesia.
"""

# 3. Fungsi Async (Worker)
async def generate_content(topic: str, platform: str) -> dict:
    # # Setup Model

    #Gemini
    # model = genai.GenerativeModel(
    #     model_name='gemini-flash-latest',
    #     system_instruction=SYSTEM_PROMPT
    # )
    
    # # Prompt Spesifik
    # user_prompt = f"Buat konten tentang '{topic}' khusus untuk platform {platform}."
    
    # print(f"🚀 Mengirim request untuk {platform}...")
    
    # # Tembak ke Google (Async)
    # response = await asyncio.to_thread(model.generate_content, user_prompt)
    
    # print(f"✅ {platform} selesai!")
    
    # return {
    #     "platform": platform,
    #     "content": response.text
    # }

    #Groq
    # Panggil API (Format standar OpenAI/Groq)
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"Buat konten {platform} soal {topic}",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    # 2. Ambil isi pesannya
    raw_content = chat_completion.choices[0].message.content

    # 3. BUNGKUS JADI DICTIONARY (Ini Solusinya!)
    # Agar formatnya sama dengan yang diharapkan oleh fungsi main()
    return {
        "platform": platform,
        "content": raw_content
    }

    #OpenAI
    # response = await client.chat.completions.create(
    #     model="gpt-4o", # <--- Model paling pintar saat ini
    #     messages=[... sama seperti di atas ...]
    # )
    # return response.choices[0].message.content

# 4. Fungsi Utama (Manager)
async def main():
    topic = input("\nMasukkan Topik Konten: ")
    print(f"\n--- Memulai Generate Parallel untuk: {topic} ---\n")
    
    start_time = time.time()
    
    # PERINTAH SAKTI: Jalankan semua worker bersamaan
    results = await asyncio.gather(
        generate_content(topic, "LinkedIn (Profesional)"),
        generate_content(topic, "Twitter Thread (Santai)"),
        generate_content(topic, "Instagram Caption (Singkat + Emoji)")
    )
    
    end_time = time.time()
    
    # Tampilkan Hasil
    print(f"\n🏁 Selesai total dalam {end_time - start_time:.2f} detik!")
    
    for item in results:
        print("\n" + "="*40)
        print(f"📱 PLATFORM: {item['platform']}")
        print("="*40)
        print(item['content'])

if __name__ == "__main__":
    asyncio.run(main())