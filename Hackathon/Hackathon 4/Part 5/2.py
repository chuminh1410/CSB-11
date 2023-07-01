inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

price_list = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

total_value = 0

for brand, quantity in inventory.items():
    price = price_list.get(brand)
    if price is not None:
        total_value += price * quantity

print("Total value of available items:", total_value)
