inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

total_products = 0

for units in inventory.values():
    total_products += units

print("Total products:", total_products)
