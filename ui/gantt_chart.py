import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def render_gantt_chart(project):
    """
    Menampilkan Gantt Chart berdasarkan
    hasil perhitungan Critical Path Method (CPM).
    """

    # Ambil seluruh aktivitas
    activities = list(project.activities.values())

    # Urutkan berdasarkan Earliest Start
    activities.sort(key=lambda x: x.es)

    # Total durasi proyek
    project_duration = max(
        activity.ef
        for activity in activities
    )

    # Membuat figure
    fig, ax = plt.subplots(figsize=(12, 6))

    y_positions = []
    y_labels = []

    # Membuat bar untuk setiap aktivitas
    for index, activity in enumerate(activities):

        y_positions.append(index)
        y_labels.append(activity.id)

        # Warna berdasarkan critical path
        color = (
            "crimson"
            if activity.is_critical
            else "steelblue"
        )

        # Panjang bar = EF - ES
        width = activity.ef - activity.es

        ax.barh(
            y=index,
            width=width,
            left=activity.es,
            height=0.5,
            color=color,
            edgecolor="black"
        )

        # Label di dalam bar
        label = (
            f"{activity.name}\n"
            f"({activity.es}-{activity.ef})"
        )

        ax.text(
            activity.es + width / 2,
            index,
            label,
            ha="center",
            va="center",
            fontsize=8,
            color="white"
        )

    # Konfigurasi sumbu
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels)

    ax.set_xlabel("Hari")
    ax.set_ylabel("Aktivitas")

    ax.set_title("Gantt Chart Project Schedule")

    # Tampilkan setiap hari
    ax.set_xticks(
        range(project_duration + 1)
    )

    ax.set_xlim(
        0,
        project_duration + 1
    )

    # Grid vertikal
    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.5
    )

    # Legend
    legend_elements = [

        Patch(
            facecolor="crimson",
            edgecolor="black",
            label="Critical Activity"
        ),

        Patch(
            facecolor="steelblue",
            edgecolor="black",
            label="Non Critical Activity"
        )

    ]

    ax.legend(handles=legend_elements)

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)