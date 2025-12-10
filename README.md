# 🚀 AI Content Generator (Multi-Platform)

Aplikasi GenAI berbasis Python yang membantu content creator membuat konten untuk LinkedIn, Twitter, dan Instagram secara **bersamaan (Parallel Async)** hanya dengan satu input topik.

![App Screenshot](assets/screenshot.png) 
*(Catatan: Nanti Anda masukkan screenshot aplikasi Anda di sini)*

## ✨ Fitur Utama
- **Multi-Provider AI:** Mendukung Google Gemini (Flash 1.5) dan Groq (Llama 3).
- **Asynchronous Execution:** Menggunakan `asyncio` untuk generate 3 konten sekaligus (3x lebih cepat dari bot biasa).
- **Interactive UI:** Dibangun dengan Streamlit yang responsif.
- **Role-Based Prompting:** Menggunakan System Instruction khusus untuk tiap platform.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** Streamlit
- **AI Models:** Google Gemini 1.5 Flash / Groq Llama 3
- **Key Concepts:** Async/Await, REST API, Prompt Engineering.

## 🚀 Cara Menjalankan (Installation)

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username-anda/ai-content-generator.git](https://github.com/username-anda/ai-content-generator.git)
   cd ai-content-generator
2. **Setup Environment**
   ``bash
   python -m venv venv
   source venv/bin/activate  # (Mac/Linux)
   # atau
   venv\Scripts\activate     # (Windows)
3. **Install Dependencies**
   ``bash
   pip install -r requirements.txt
4. **Setup API Key Buat file .env dan isi:**
   GOOGLE_API_KEY=masukkan_api_key_disini
5. **Run App**
   ``bash
   streamlit run app.py

👨‍💻 Author
[Nama Anda] Aspiring AI Engineer | Python Developer [Link LinkedIn Anda]

---

### 📸 Langkah 3: Ambil Screenshot (Bukti Nyata)
1.  Jalankan aplikasi Anda.
2.  Isi topik, klik Generate, tunggu sampai muncul 3 kolom.
3.  **Screenshot** tampilan browsernya yang rapi.
4.  Buat folder baru di project bernama `assets`.
5.  Simpan gambar tadi di sana dengan nama `screenshot.png`.

*Efek Psikologis:* Klien freelance lebih percaya melihat **Gambar UI** daripada melihat kode ruwet.

---

### 🚀 Langkah 4: Upload ke GitHub
Jika Anda belum terbiasa pakai Terminal Git, pakai cara termudah (Drag & Drop) dulu tidak apa-apa untuk awal:

1.  Login ke GitHub.com.
2.  Klik **New Repository**.
3.  Nama: `ai-content-generator`. (Pilih **Public**).
4.  Klik **Create Repository**.
5.  Klik link kecil: **"uploading an existing file"**.
6.  Drag & Drop file berikut dari folder komputer Anda:
    * `app.py`
    * `requirements.txt`
    * `README.md`
    * Folder `assets` (beserta isinya)
    * **JANGAN UPLOAD:** `.env` atau folder `venv`.
7.  Klik **Commit changes**.

---

### ✅ Checklist Final "Zero-to-Pro"
Coba cek repo Anda nanti:
1.  [ ] Apakah ada screenshot di halaman depan?
2.  [ ] Apakah file `.env` **TIDAK** ada di sana? (Wajib!)
3.  [ ] Apakah deskripsi menjelaskan teknologi "Async" dan "AI"? (Ini buzzword mahal).