import nicegui
import os

def get_folder():
    file_path = os.path.abspath(__file__)

    dir_path = os.path.dirname(file_path)

    records_folder = os.path.join(dir_path, "Records")

    return records_folder



if __name__ == "__main__":
    print(get_folder())