import os


def get_csv_file_path(path: str) -> str:
    file = None

    for file in os.listdir(path):
        if file.endswith(".csv"):
            file = path + "/" + file

    return file