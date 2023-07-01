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

brand = input("Input a brand: ")
units = int(input("Input amount to buy: "))

price = price_list.get(brand)
if price is not None:
    total = units * price
    print("Total price:", total)

    stock = inventory.get(brand)
    if stock is not None and units <= stock:
        remaining = stock - units
        inventory[brand] = remaining

    print("Available products:")
    for brand, units in inventory.items():
        print("-", brand + ":", units)
else:
    print("Brand not found in the price list.")
