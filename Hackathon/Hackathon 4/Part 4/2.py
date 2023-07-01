price_list = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

brand = input("Input a brand: ")
units = int(input("Input amount to buy: "))

if brand in price_list:
    price = price_list[brand]
    total = units * price
    print("Total price:", total)
else:
    print("Brand not found in the price list.")
