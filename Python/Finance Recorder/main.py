import os
import csv
import sys
from PySide6 import QtCore, QtWidgets, QtGui

import gui

headers = ["Date", "Record name", "Change in value"]

test_entry = ["Test", "Test", "Test"]

test_data = dict(zip(headers, test_entry))

def get_folder():
    file_path = os.path.abspath(__file__)

    dir_path = os.path.dirname(file_path)

    records_folder = os.path.join(dir_path, "Records")

    return records_folder

def create_new_record(record_path):
    with open(record_path, "w", newline="") as record:
        writer = csv.DictWriter(record, fieldnames=headers)
        writer.writeheader()
        writer.writerow(test_data)

def create_new_entry(record_path):
    with open(record_path, "a", newline="") as record:
        writer = csv.DictWriter(record, fieldnames=headers)
        writer.writerow(test_data)

def get_record(name, records_folder):
    record_path = os.path.join(records_folder, name) + ".csv"

    if not os.path.isfile(record_path):
        create_new_record(record_path)
    else:
        create_new_entry(record_path)

if __name__ in {"__main__", "__mp_main__"}:
    app = QtWidgets.QApplication([])

    widget = gui.test()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())