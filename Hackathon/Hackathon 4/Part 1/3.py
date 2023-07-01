inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

brand = input("Input a brand: ")

if brand in inventory:
    so_luong = inventory[brand]
    print("Available", brand + "s :", so_luong)
else:
    print("Không có", brand, "trong kho.")
