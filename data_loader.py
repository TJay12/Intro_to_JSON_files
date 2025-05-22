import json
from pathlib import Path

def load_json(filename):
    path = Path("data") / filename
    with open(path, "r") as file:
        return json.load(file)

def save_json(filename, data):
    path = Path("data") / filename
    with open(path, "w") as file:
        json.dump(data, file, indent=4)