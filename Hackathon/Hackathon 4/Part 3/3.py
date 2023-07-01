price_list = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

brand = input("Nhập hãng máy: ")

if brand in price_list:
    price = price_list[brand]
    print("Price of", brand + ":", price)
else:
    print("Brand not found in the price list.")
