import streamlit as st


def render_input_form():
    """
    Menampilkan form input aktivitas.
    Mengembalikan list activities.
    """

    jumlah_aktivitas = st.number_input(
        "Jumlah Aktivitas",
        min_value=1,
        value=1,
        step=1
    )

    st.divider()

    activities = []

    st.header("Input Data Aktivitas")

    for i in range(jumlah_aktivitas):

        st.subheader(f"Aktivitas {i + 1}")

        col1, col2, col3 = st.columns(3)

        with col1:
            activity_id = st.text_input(
                "ID Aktivitas",
                key=f"id_{i}"
            )

        with col2:
            activity_name = st.text_input(
                "Nama Aktivitas",
                key=f"name_{i}"
            )

        with col3:
            duration = st.number_input(
                "Durasi",
                min_value=1,
                value=1,
                key=f"duration_{i}"
            )

        dependency = st.text_input(
            "Dependency (pisahkan dengan koma)",
            key=f"dependency_{i}",
            placeholder="Contoh: A,B"
        )

        activities.append({

            "id": activity_id.strip(),

            "name": activity_name.strip(),

            "duration": duration,

            "dependency": dependency.strip()

        })

        st.divider()

    return activities