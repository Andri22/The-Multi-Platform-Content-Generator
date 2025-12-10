import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
import google.generativeai as genai
from groq import AsyncGroq

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

SYSTEM_PROMPT = """
Kamu adalah Expert Social Media Strategist. 
Gaya bahasa kamu menarik, viral, tapi tetap profesional.
Selalu gunakan Bahasa Indonesia.
"""

# --- 2. BACKEND LOGIC (Worker) ---
# Ini fungsi yang sama persis dengan yang kita buat sebelumnya
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

# --- 3. FRONTEND LOGIC (UI) ---
def main():
    # Judul
    st.title("🚀 Multi-Platform Content Generator")
    st.write("Satu topik, tiga konten, **sekali klik**.")

    # Input User
    topic_input = st.text_input("Mau posting soal apa hari ini?", placeholder="Misal: Tips Coding untuk Pemula")

    # Tombol Action
    if st.button("Generate Konten"):
        if not topic_input:
            st.warning("Isi topiknya dulu dong bos!")
        else:
            # Tampilkan Loading Spinner
            with st.spinner("AI sedang berpikir keras..."):
                
                # --- JEMBATAN ASYNC KE SYNC ---
                # Streamlit aslinya sync, jadi kita bungkus proses async di sini
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                results = loop.run_until_complete(asyncio.gather(
                    generate_content(topic_input, "LinkedIn"),
                    generate_content(topic_input, "Twitter Thread"),
                    generate_content(topic_input, "Instagram Caption")
                ))
                
            # --- TAMPILKAN HASIL (3 KOLOM) ---
            st.success("Selesai! Silakan copy-paste.")
            
            # Membagi layar jadi 3 kolom
            col1, col2, col3 = st.columns(3)

            with col1:
                st.header("👔 LinkedIn")
                st.info(results[0]['content']) # Ambil hasil pertama
            
            with col2:
                st.header("🐦 Twitter")
                st.success(results[1]['content']) # Ambil hasil kedua

            with col3:
                st.header("📸 Instagram")
                st.warning(results[2]['content']) # Ambil hasil ketiga

# Menjalankan App
if __name__ == "__main__":
    main()