from data_loader import load_json

fruits = load_json("fruits.json")

for fruit, info in fruits.items():
    print(f"{fruit.title()} is {info['color']} and costs ${info['price']}")