# OpenClaw2026_SupandiSaputra_NaviAgent

# 🤖 Navi: Intelligent TikTok Community Agent

**Navi** adalah AI Agent otomatis yang dirancang untuk mengelola interaksi komunitas pada platform TikTok secara *real-time*. Menggunakan kombinasi *Agentic Workflow* dan *Infrastructure-as-Code*, Navi mampu memahami konteks komentar dan memberikan respon yang relevan dalam hitungan detik.

## 🚀 Panduan Uji Coba (Live Testing)

Juri tidak perlu melakukan instalasi apa pun. Untuk melihat Navi beraksi secara langsung, silakan ikuti langkah berikut:

1.  **Buka TikTok:** Kunjungi profil **[@english.rizz](https://www.tiktok.com/@english.rizz)**.
2.  **Pilih Postingan:** Pilih salah satu video terbaru yang ada di akun tersebut.
3.  **Kirim Komentar:** Berikan komentar apa pun (bisa berupa sapaan, pertanyaan tentang bahasa Inggris, atau sekadar tes).
4.  **Pantau Respon:** Tunggu beberapa saat (15-30 detik) agar Navi memproses *webhook*, berpikir melalui QwenPaw, dan mengirimkan balasan otomatis ke komentar Anda.

---

## 🛠️ Tech Stack & Arsitektur

Proyek ini dibangun dengan fokus pada **Persistence** (ketahanan) dan **Scalability** (skalabilitas):

* **Logic Bridge:** FastAPI & Python (Dijalankan di Sumopod).
* **AI Brain:** QwenPaw Agent berbasis AgentScope Runtime.
* **Automation Broker:** Repliz (Webhook & TikTok API Integration).
* **Connectivity:** Cloudflare Tunnel (Secure tunneling dari local-to-web).
* **Process Management:** **PM2** (Memastikan sistem tetap *online* 24/7 dan melakukan *auto-restart* jika terjadi kegagalan).

---

## 🔄 Workflow System

1.  **Trigger:** Juri memberikan komentar di akun TikTok @english.rizz.
2.  **Ingestion:** Repliz menangkap komentar dan mengirimkan *payload* JSON ke server FastAPI via Cloudflare Tunnel.
3.  **Processing:** `main.py` melakukan parsing data dan mengirimkan instruksi ke Agen Navi di QwenPaw.
4.  **Cognition:** Navi menganalisis maksud komentar dan menentukan aksi terbaik (Like/Reply).
5.  **Action:** Navi mengeksekusi *Skill* API untuk mengirimkan balasan kembali ke TikTok via Repliz.

---

## 💡 Impact & Future Development

* **Impact:** Implementasi sistem ini berhasil mengotomatisasi manajemen komunitas secara penuh sehingga meningkatkan kecepatan respon dan efisiensi keterlibatan pengguna.
* **Future Development:** Pengembangan masa depan akan difokuskan pada integrasi memori jangka panjang dan orkestrasi multi-agen untuk menangani tugas-tugas yang jauh lebih kompleks.

---
**Developed by:** Supandi Saputra (Pandi)
