from core.activity import Activity
from core.graph import ProjectGraph


def build_project(activities):
    """
    Membangun ProjectGraph dari data input pengguna.

    Parameters
    ----------
    activities : list
        List berisi dictionary aktivitas.

    Returns
    -------
    ProjectGraph
    """

    project = ProjectGraph()

    # ==========================
    # VALIDASI INPUT
    # ==========================

    for item in activities:

        if item["id"] == "":
            raise ValueError(
                "ID Aktivitas tidak boleh kosong."
            )

        if item["name"] == "":
            raise ValueError(
                "Nama Aktivitas tidak boleh kosong."
            )

    # ==========================
    # MEMBUAT ACTIVITY
    # ==========================

    for item in activities:

        activity = Activity(
            activity_id=item["id"],
            name=item["name"],
            duration=int(item["duration"])
        )

        project.add_activity(activity)

    # ==========================
    # VALIDASI DEPENDENCY
    # ==========================

    available_ids = {

        item["id"]

        for item in activities

    }

    for item in activities:

        dependency_text = item["dependency"]

        if dependency_text != "":

            dependencies = [

                dep.strip()

                for dep in dependency_text.split(",")

            ]

            for dep in dependencies:

                if dep not in available_ids:

                    raise ValueError(

                        f"Dependency '{dep}' pada aktivitas '{item['id']}' tidak ditemukan."

                    )

    # ==========================
    # TAMBAHKAN DEPENDENCY
    # ==========================

    for item in activities:

        dependency_text = item["dependency"]

        if dependency_text != "":

            dependencies = [

                dep.strip()

                for dep in dependency_text.split(",")

            ]

            for dep in dependencies:

                project.add_dependency(
                    dep,
                    item["id"]
                )

    # ==========================
    # DETEKSI CYCLE
    # ==========================

    if project.has_cycle():

        raise ValueError(
            "Graph mengandung Circular Dependency."
        )

    return project