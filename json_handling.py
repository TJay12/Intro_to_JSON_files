import json
from pathlib import Path

# More Advanced read/write
DATA_FOLDER = Path("data")

def load_json(filename):
    path = DATA_FOLDER / filename
    if not path.exists():
        print(f"{filename} not found.")
        return {}
    with path.open("r") as file:
        return json.load(file)

def save_json(filename, data):
    path = DATA_FOLDER / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as file:
        json.dump(data, file, indent=4)

def create_blank_json_file(filename):
    save_json(filename, {})
    print(f"{filename} created")

def initial_write_file():
    filename = input("Filename: ")
    path = DATA_FOLDER / filename

    with path.open("w") as file:
        dictionary = input("Dict Name: ")
        items = int(input(f"How many {dictionary} adding: "))

        dictionary = {}

        for num in range(items):
            item = input("Name: ")
            color = input("Color: ")
            price = float(input("Price: "))
            dictionary[item] = {"color": color, "price": price}

        json.dump(dictionary, file, indent=4)

    print(f"{items} items added to {filename}")

initial_write_file()