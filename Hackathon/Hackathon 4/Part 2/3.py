inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

inventory['DELL'] = 60  
inventory['MACBOOK'] = 2  

print("Available products:")
for brand, units in inventory.items():
    print("-", brand + ":", units)
