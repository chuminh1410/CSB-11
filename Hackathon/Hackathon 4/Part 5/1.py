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

total = {}

for brand, quantity in inventory.items():
    price = price_list.get(brand)
    if price is not None:
        total[brand] = price * quantity

print("Total value of available brands:")
for brand, value in total.items():
    print("-", brand + ":", value)
