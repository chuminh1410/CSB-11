n = int(input("Input a number: "))

if n <= 0:
    print("Invalid input. Enter a number greater than 0.")
else:
    for num in range(1, n + 1, 2):
        print(num)
