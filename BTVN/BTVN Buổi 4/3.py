number = int(input("Input number: "))

if number < 0:
    print("Invalid")
else:
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"{number}! = {result}")