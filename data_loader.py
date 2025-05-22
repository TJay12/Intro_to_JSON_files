import json
from pathlib import Path

# Basic read/write
def load_json_basic(filename):
    path = Path("data") / filename
    with open(path, "r") as file:
        return json.load(file)

def save_json_basic(filename, data):
    path = Path("data") / filename
    with open(path, "w") as file:
        json.dump(data, file, indent=4)