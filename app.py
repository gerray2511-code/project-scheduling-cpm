import streamlit as st

from core.cpm import CPMCalculator
from core.project_builder import build_project

from ui.input_form import render_input_form
from ui.result_view import render_result
from ui.graph_view import render_graph
from ui.gantt_chart import render_gantt_chart


# ==================================================
# KONFIGURASI HALAMAN
# ==================================================

st.set_page_config(
    page_title="Project Scheduling with CPM",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("📊 Project Scheduling")

    st.markdown("---")

    st.subheader("🏠 Home")

    st.write(
        """
Sistem ini digunakan untuk melakukan
analisis penjadwalan proyek menggunakan
algoritma **Critical Path Method (CPM)**.
        """
    )

    st.markdown("---")

    st.subheader("🧑‍💻 Informasi Aplikasi")

    st.write("**Nama:** Project Scheduling with CPM")
    st.write("**Versi:** 1.0")
    st.write("**Framework:** Streamlit")

    st.markdown("---")

    st.subheader("📚 Struktur Data")

    st.success("Graph")
    st.success("Adjacency List")
    st.success("Queue (Deque)")

    st.markdown("---")

    st.subheader("⚙️ Algoritma")

    st.info("Topological Sort")
    st.info("Forward Pass")
    st.info("Backward Pass")
    st.info("Critical Path Method (CPM)")

    st.markdown("---")

    with st.expander("📖 Tentang CPM"):

        st.write(
            """
Critical Path Method (CPM) adalah metode
manajemen proyek yang digunakan untuk
mengidentifikasi jalur kritis (Critical Path)
dan menghitung estimasi waktu minimum
penyelesaian suatu proyek.

Aplikasi ini memanfaatkan:

- Graph
- Adjacency List
- Queue (Deque)
- Topological Sort
- Forward Pass
- Backward Pass

untuk melakukan analisis penjadwalan proyek.
            """
        )

    st.markdown("---")

    st.caption("© 2026 Project Scheduling with CPM")


# ==================================================
# HEADER
# ==================================================

st.title("📊 Sistem Penjadwalan Proyek")

st.subheader("Critical Path Method (CPM)")

st.markdown(
    """
Aplikasi ini digunakan untuk melakukan analisis
penjadwalan proyek menggunakan algoritma
**Critical Path Method (CPM)**.

Masukkan daftar aktivitas proyek beserta
durasi dan dependency untuk memperoleh:

- Earliest Start (ES)
- Earliest Finish (EF)
- Latest Start (LS)
- Latest Finish (LF)
- Slack
- Critical Path
- Total Durasi Proyek

Selain itu aplikasi juga menampilkan
visualisasi dependency graph dan Gantt Chart.
"""
)

st.divider()

# ==================================================
# INPUT FORM
# ==================================================

activities = render_input_form()

# ==================================================
# SIDEBAR STATISTIK
# ==================================================

with st.sidebar:

    st.markdown("---")

    st.subheader("📊 Statistik")

    st.metric(
        "Jumlah Aktivitas",
        len(activities)
    )

# ==================================================
# TOMBOL HITUNG
# ==================================================

if st.button(
    "🚀 Hitung CPM",
    use_container_width=True
):

    try:

        # ------------------------------------------
        # Bangun Graph
        # ------------------------------------------

        project = build_project(
            activities
        )

        # ------------------------------------------
        # Jalankan CPM
        # ------------------------------------------

        calculator = CPMCalculator(
            project
        )

        result = calculator.calculate()

        # ------------------------------------------
        # Hasil Analisis
        # ------------------------------------------

        render_result(result)

        # ------------------------------------------
        # Dependency Graph
        # ------------------------------------------

        st.divider()

        st.header("🕸️ Visualisasi Dependency Graph")

        render_graph(project)

        # ------------------------------------------
        # Gantt Chart
        # ------------------------------------------

        st.divider()

        st.header("📅 Gantt Chart")

        render_gantt_chart(project)

    except Exception as error:

        st.error(
            f"❌ Terjadi kesalahan: {error}"
        )