from data_loader import load_json, save_json

fruits = load_json("fruits.json")

for fruit, info in fruits.items():
    print(f"{fruit.title()} is {info['color']} and costs ${info['price']}")

print(f"{'*' * 18}")
print(f"{'Sale':^18}")
print(f"{'*' * 18}")
for fruit, info in fruits.items():
    print(f"{fruit.title()}s only {info['price']}")
print(f"{'*' * 18}")

def add_fruit():
    fruits = load_json("fruits.json")

    new_fruit = input("Fruit: ").lower()
    fruit_color = input("Fruit Color: ").lower()
    try:
        fruit_price = float(input("Fruit Price: "))
    except ValueError:
        print("Price must be a number")
        return

    if new_fruit in fruits:
        print(f"{new_fruit} already exists. Overwriting")

    add_new_fruit = {
        new_fruit: {
            "color": fruit_color,
            "price": fruit_price
        }
    }

    fruits.update(add_new_fruit)

    save_json("fruits.json", fruits)

    print(f"{new_fruit} added")

