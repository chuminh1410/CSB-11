ordered_dishes = []

print("== Welcome to MindX Resturant ==")

while True:
    dish = input("Please choose a dish: ")
    
    if dish in ordered_dishes:
        print("You have this in the order already")
    else:
        ordered_dishes.append(dish)
        print("Great choice!")
    choice = input("Anything else? (y/n): ")
    if choice.lower() != "y":
        break
    
print("Well done! Your order:")
for dish in ordered_dishes:
    print(f"- {dish}")