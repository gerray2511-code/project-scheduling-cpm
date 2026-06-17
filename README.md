# 📊 Project Scheduling System using Critical Path Method (CPM)

## 📌 Deskripsi

Project ini merupakan implementasi **Critical Path Method (CPM)** untuk membantu proses penjadwalan proyek menggunakan konsep **Graph** sebagai struktur data utama.

Aplikasi dibangun menggunakan **Python** dan **Streamlit** sehingga pengguna dapat memasukkan daftar aktivitas beserta durasi dan dependency untuk memperoleh analisis jadwal proyek secara otomatis.

---

# 🎯 Tujuan Project

Tujuan dari project ini adalah:

- Membantu menghitung estimasi durasi penyelesaian proyek.
- Menentukan jalur kritis (Critical Path).
- Mengidentifikasi aktivitas yang memiliki slack.
- Memvisualisasikan hubungan antar aktivitas menggunakan Graph.
- Menampilkan Gantt Chart sebagai representasi jadwal proyek.

---

# 🧠 Struktur Data yang Digunakan

Project ini mengimplementasikan beberapa konsep Struktur Data, yaitu:

- Graph
- Adjacency List
- Queue (Deque)

---

# ⚙️ Algoritma yang Digunakan

Algoritma utama yang digunakan pada project ini adalah:

- Topological Sort (Kahn Algorithm)
- Forward Pass
- Backward Pass
- Slack Calculation
- Critical Path Method (CPM)

---

# 🏗️ Arsitektur Project

```
project-cpm/
│
├── app.py
│
├── core/
│   ├── activity.py
│   ├── graph.py
│   ├── cpm.py
│   └── project_builder.py
│
├── ui/
│   ├── input_form.py
│   ├── result_view.py
│   ├── graph_view.py
│   └── gantt_chart.py
│
├── utils/
│   └── file_handler.py
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Cara Menjalankan Project

## Clone Repository

```bash
git clone https://github.com/username/project-cpm.git
```

Masuk ke folder project

```bash
cd project-cpm
```

Install dependency

```bash
pip install -r requirements.txt
```

Jalankan aplikasi

```bash
streamlit run app.py
```

---

# 📷 Fitur Utama

- Input aktivitas proyek
- Input dependency antar aktivitas
- Perhitungan CPM otomatis
- Perhitungan ES, EF, LS, LF
- Perhitungan Slack
- Penentuan Critical Path
- Visualisasi Dependency Graph
- Visualisasi Gantt Chart

---

# 📈 Contoh Studi Kasus

| ID | Aktivitas | Durasi | Dependency |
|----|-----------|---------|------------|
| A | Analisis | 3 | - |
| B | Desain | 2 | A |
| C | Backend | 4 | A |
| D | Testing | 2 | B,C |
| E | Deploy | 1 | D |

---

# 🖥️ Teknologi

- Python
- Streamlit
- NetworkX
- Matplotlib
- Pandas

---

# 📚 Mata Kuliah

Struktur Data dan Pemrograman

---

# 👨‍🎓 Author

Nama: **Geraldus Rayen, Fabio Satya Ar-Rasy**

Universitas: **Institute Teknologi dan Bisnis Bina Sarana Global**

Tahun: **2026**

---

# 📄 Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran.