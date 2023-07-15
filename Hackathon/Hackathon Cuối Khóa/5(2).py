phone_price = {
    "Iphone12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000
}

budget = int(input("Input your budget: "))
in_budget = []
for phone, price in phone_price.items():
    if price <= budget:
        in_budget.append(phone)

print("Phone that fit your budget:")
for phone in in_budget:
    print("-", phone + ":", phone_price[phone])