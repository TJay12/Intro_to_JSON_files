from data_loader import load_json

fruits = load_json("fruits.json")

for fruit, info in fruits.items():
    print(f"{fruit.title()} is {info['color']} and costs ${info['price']}")

print(f"{'*' * 18}")
print(f"{'Sale':^18}")
print(f"{'*' * 18}")
for fruit, info in fruits.items():
    print(f"{fruit.title()}s only {info['price']}")
print(f"{'*' * 18}")