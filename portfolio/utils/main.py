import json
import os


def read_data():
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(file_path, "r") as file:
        links = json.load(file)
        return links
