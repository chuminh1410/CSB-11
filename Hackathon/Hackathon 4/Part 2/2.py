inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

brand = input("Nhập loại máy: ")
units = int(input("Nhập số lượng: "))

inventory[brand] = units  
print("Available products:")
for brand, units in inventory.items():
    print("-", brand + ":", units)
