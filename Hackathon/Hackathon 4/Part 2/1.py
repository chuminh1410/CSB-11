inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

inventory['TOSHIBA'] = 10  

print("Available products:")
for brand, units in inventory.items():
    print("-", brand + ":", units)
