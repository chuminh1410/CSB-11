phone_price = {
    "Iphone12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000
}

name = input("Input name of a phone: ")
price = phone_price[name]
print(f"Price of {name}: {price}")