from data_loader import load_json

animals = load_json("animals.json")

for animal, info in animals.items():
    print(f"A {animal} goes '{info['sound']}' and has {info['legs']} legs")