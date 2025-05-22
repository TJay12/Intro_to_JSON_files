import json

character = {
    "name": "TJ the Brave",
    "level": 1,
    "total exp": 0,
    "next level": 30,
    "class": "Wizard",
    "inventory": ["wand", "cloak", "mana potion"],
    "location": {"x": 10, "y": 42}
}

def save_file():
    with open("data/character.json", "w") as file:
        json.dump(character, file, indent=4)

def view_save():
    with open("data/character.json", "r") as file:
        saved_char = json.load(file)

    print(f"{saved_char['name']} is at level {saved_char['level']} with {saved_char['inventory']}")

def load_save():
    with open("data/character.json", "r") as file:
        saved_char = json.load(file)
        character["name"] = saved_char['name']
        character["level"] = saved_char['level']
        character["total exp"] = saved_char['total exp']
        character["next level"] = saved_char['next level']
        character["class"] = saved_char['class']
        character["inventory"] = saved_char['inventory']
        character["location"] = saved_char['location']

def level_up_check():
    if character['total exp'] >= character['next level']:
        character['level'] += 1
        character['next level'] += character['next level'] * 0.6

def add_exp():
    exp_gain  = int(input("Exp: "))
    character['total exp'] += exp_gain
    level_up_check()

# save_file()
# view_save()

# load_save()
# add_exp()
# print("Total exp: ", character['total exp'])
# print("Next Level at: ", character['next level'])
# save_file()