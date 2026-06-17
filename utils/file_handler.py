import json


def save_project(filename, activities):
    """
    Menyimpan data aktivitas ke file JSON.
    """

    data = {
        "activities": activities
    }

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_project(filename):
    """
    Membaca data aktivitas dari file JSON.
    """

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data["activities"]