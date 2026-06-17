import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


def render_graph(project):
    """
    Menampilkan visualisasi dependency graph.
    """

    # Membuat graph terarah
    G = nx.DiGraph()

    # Tambahkan node
    for activity in project.activities.values():
        G.add_node(activity.id)

    # Tambahkan edge
    for source in project.graph:

        for target in project.graph[source]:

            G.add_edge(source, target)

    # Menentukan warna node
    node_colors = []

    for node in G.nodes():

        activity = project.activities[node]

        if activity.is_critical:
            node_colors.append("red")
        else:
            node_colors.append("skyblue")

    # Layout graph
    pos = nx.spring_layout(
        G,
        seed=42,
        k=2
    )

    # Membuat figure
    fig, ax = plt.subplots(figsize=(10, 7))

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        node_size=2500,
        ax=ax
    )

    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True,
        arrowsize=25,
        ax=ax
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=11,
        font_weight="bold",
        ax=ax
    )

    ax.set_title(
        "Visualisasi Dependency Graph",
        fontsize=14
    )

    ax.axis("off")

    st.pyplot(fig)