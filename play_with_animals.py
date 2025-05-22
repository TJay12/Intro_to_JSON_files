from data_loader import load_json_basic, save_json_basic

animals = load_json_basic("animals.json")

print(f"\nFour legged friends!")
for animal, info in animals.items():
    if info['legs'] == 4:
        print(f" - {animal}")

print("")
for animal, info in animals.items():
    print(f"A {animal} goes '{info['sound']}'")

def add_animal():
    animals = load_json_basic("animals.json")

    new_animal = input("Animal: ").lower()
    animal_sound = input("Animal Sound: ").lower()
    try:
        animal_legs = int(input("Animal Legs: "))
    except ValueError:
        print("Price must be a number")
        return

    if new_animal in animals:
        print(f"{new_animal} already exists. Overwriting")

    add_new_animal = {
        new_animal: {
            "sound": animal_sound,
            "legs": animal_legs
        }
    }

    animals.update(add_new_animal)

    save_json_basic("animals.json", animals)

    print(f"{new_animal} added")
