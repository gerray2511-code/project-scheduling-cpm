import streamlit as st

from core.cpm import CPMCalculator
from core.project_builder import build_project

from ui.input_form import render_input_form
from ui.result_view import render_result
from ui.graph_view import render_graph
from ui.gantt_chart import render_gantt_chart

from utils.file_handler import save_project


# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Project Scheduling with CPM",
    page_icon="📊",
    layout="wide"
)


# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 Project Scheduling")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Beranda",
        "📋 Analisis CPM",
        "📖 Panduan",
        "ℹ️ Tentang"
    ]
)


# =====================================
# BERANDA
# =====================================

if menu == "🏠 Beranda":

    st.title("📊 Sistem Penjadwalan Proyek")

    st.subheader("Critical Path Method (CPM)")

    st.markdown(
        """
Selamat datang pada aplikasi **Project Scheduling with
Critical Path Method (CPM)**.

Aplikasi ini dikembangkan untuk membantu pengguna dalam
melakukan analisis penjadwalan proyek berdasarkan
hubungan ketergantungan (dependency) antar aktivitas.

### Fitur Utama

- ✅ Input aktivitas proyek
- ✅ Input dependency
- ✅ Perhitungan Critical Path Method (CPM)
- ✅ Perhitungan ES, EF, LS, LF
- ✅ Perhitungan Slack
- ✅ Menentukan Critical Path
- ✅ Visualisasi Dependency Graph
- ✅ Visualisasi Gantt Chart

Gunakan menu **Analisis CPM** untuk mulai melakukan
perhitungan proyek.
"""
    )


# =====================================
# ANALISIS CPM
# =====================================

elif menu == "📋 Analisis CPM":

    st.title("📋 Analisis Critical Path Method")

    st.markdown(
        """
Masukkan data aktivitas proyek beserta durasi dan
dependency untuk dilakukan analisis menggunakan
algoritma **Critical Path Method (CPM)**.
"""
    )

    st.divider()

    activities = render_input_form()

    st.divider()

    if st.button(
        "🚀 Hitung CPM",
        use_container_width=True
    ):

        try:

            project = build_project(
                activities
            )

            calculator = CPMCalculator(
                project
            )

            result = calculator.calculate()

            save_project(
                "project.json",
                activities
            )

            render_result(result)

            st.divider()

            st.header("🕸️ Dependency Graph")

            render_graph(project)

            st.divider()

            st.header("📅 Gantt Chart")

            render_gantt_chart(project)

        except Exception as e:

            st.error(str(e))


# =====================================
# PANDUAN
# =====================================

elif menu == "📖 Panduan":

    st.title("📖 Panduan Penggunaan")

    st.markdown(
        """
## Langkah 1

Masukkan jumlah aktivitas proyek.

---

## Langkah 2

Isi data setiap aktivitas:

- ID Aktivitas
- Nama Aktivitas
- Durasi
- Dependency

Dependency dapat lebih dari satu.

Contoh:


---

## Langkah 3

Klik tombol:


---

## Langkah 4

Sistem akan menghitung:

- Earliest Start (ES)
- Earliest Finish (EF)
- Latest Start (LS)
- Latest Finish (LF)
- Slack
- Critical Path

---

## Langkah 5

Hasil analisis akan ditampilkan dalam bentuk:

- Ringkasan proyek
- Tabel hasil CPM
- Dependency Graph
- Gantt Chart

---

Pastikan dependency yang dimasukkan sudah benar agar
perhitungan dapat dilakukan dengan optimal.
"""
    )


# =====================================
# TENTANG
# =====================================

elif menu == "ℹ️ Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown(
        """
## Project Scheduling with Critical Path Method

Aplikasi ini merupakan implementasi algoritma
**Critical Path Method (CPM)** menggunakan
bahasa pemrograman Python.

### Tujuan

Membantu melakukan analisis manajemen waktu proyek
dengan menentukan jalur kritis dan estimasi durasi
penyelesaian proyek.

---

## Struktur Data yang Digunakan

- Graph
- Adjacency List

---

## Algoritma yang Digunakan

- Topological Sort
- Forward Pass
- Backward Pass
- Slack Calculation
- Critical Path Method (CPM)

---

## Teknologi

- Python
- Streamlit
- NetworkX
- Matplotlib
- Pandas

---

Dikembangkan sebagai project implementasi
**Struktur Data dan Pemrograman**.
"""
    )
