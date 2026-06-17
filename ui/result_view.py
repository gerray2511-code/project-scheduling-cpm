import streamlit as st
import pandas as pd


def render_result(result):

    st.header("📈 Hasil Analisis CPM")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Aktivitas",
            result["total_activities"]
        )

    with col2:

        st.metric(
            "Aktivitas Kritis",
            result["critical_count"]
        )

    with col3:

        st.metric(
            "Durasi Proyek",
            f'{result["project_duration"]} Hari'
        )

    st.divider()

    st.subheader("🔥 Critical Path")

    critical_path = " → ".join(
        result["critical_path"]
    )

    st.success(critical_path)

    st.divider()

    table = []

    activities = sorted(
        result["activities"].values(),
        key=lambda x: x.es
    )

    for activity in activities:

        table.append({

            "ID": activity.id,

            "Nama": activity.name,

            "Durasi": activity.duration,

            "Earliest Start": activity.es,

            "Earlist Finish": activity.ef,

            "Latest Start": activity.ls,

            "Latest Finish": activity.lf,

            "Slack": activity.slack,

            "Critical":

                "Ya"

                if activity.is_critical

                else "Tidak"

        })

    df = pd.DataFrame(table)

    st.subheader("📋 Tabel Hasil CPM")

    st.dataframe(
        df,
        use_container_width=True
    )