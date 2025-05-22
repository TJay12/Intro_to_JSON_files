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

    new_fruit = input("Fruit: ")
    fruit_color = input("Fruit Color: ")
    fruit_price = float(input("Fruit Price: "))

    add_new_fruit = {
        new_fruit: {
            "color": fruit_color,
            "price": fruit_price
        }
    }

    fruits.update(add_new_fruit)

    save_json("fruits.json", fruits)

    print(f"{new_fruit} added")

add_fruit()