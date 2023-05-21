def calculate_average_price(menu):
    total_price = 0
    for item in menu:
        total_price += item[1]
    average_price = total_price / len(menu)
    return average_price

def filter_items_above_average(menu, average_price):
    items_above_average = []
    for item in menu:
        if item[1] > average_price:
            items_above_average.append(item)
    return items_above_average

n = int(input("Number of items: "))

menu = []
for i in range(n):
    item_name = input(f"Item {i+1}: ")
    item_price = float(input(f"Price of item {i+1}: "))
    menu.append((item_name, item_price))

average_price = calculate_average_price(menu)

print("Average price:", average_price)

items_above_average = filter_items_above_average(menu, average_price)
print("Item(s) above average price:", end=" ")
for item in items_above_average:
    print(item, end=" ")
