from json_handling import save_json, load_json

veggies = {
    "carrot": {
        "color": "orange",
        "price": 0.2
    },
    "lettuce": {
        "color": "green",
        "price": 0.5
    }
}

save_json("veggies.json", veggies)
print("Initial veggies written")

# Read and display
def read_veggies():
    veggies = load_json("veggies.json")

    for veg, info in veggies.items():
        print(f"{veg.title()} is {info['color']} and costs {info['price']}")

read_veggies()