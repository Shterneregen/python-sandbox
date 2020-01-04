from pathlib import Path


def show_files():
    path = Path()
    for file in path.glob('*.*'):
        print(file)


def show_all():
    path = Path()
    for file in path.glob('*'):
        print(file)


def read_file(file_path):
    path = Path(file_path)
    if path.exists():
        print(path.read_text())
    else:
        print("File doesn't exist")


def open_file(file_path):
    try:
        file = open(file_path, "r")
        for line in file:
            print(line)
    except FileNotFoundError:
        print("File not found!")
