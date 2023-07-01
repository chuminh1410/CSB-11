character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}

skills = [
    {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    },
    {
        "Name": "Quick Attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5
    },
    {
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2
    }
]

while True:
    print("Skills:")
    for i, skill in enumerate(skills, start=1):
        print(f"Skill {i}: {skill['Name']}")

    choice = int(input("Choose skill by number: "))

    if choice < 1 or choice > len(skills):
        print("Invalid choice. Please choose a valid skill number.")
        continue

    selected_skill = skills[choice - 1]

    if character["Level"] < selected_skill["Minimum level"]:
        print("Cannot deploy. Required level", selected_skill["Minimum level"])
    else:
        print("You chose", selected_skill["Name"])
        print("Damage:", selected_skill["Damage"])
        break
