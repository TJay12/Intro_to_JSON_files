from data_loader import load_json

animals = load_json("animals.json")

print(f"\nFour legged friends!")
for animal, info in animals.items():
    if info['legs'] == 4:
        print(f" - {animal}")

print("")
for animal, info in animals.items():
    print(f"A {animal} goes '{info['sound']}'")
