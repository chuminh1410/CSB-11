numbers = [5, 1, 8, 92, -1, 30]
search_number = int(input("Input a number: "))

if search_number in numbers:
    position = numbers.index(search_number) + 1
    print(f"Number found at position {position}")
else:
    print("Number not found")
