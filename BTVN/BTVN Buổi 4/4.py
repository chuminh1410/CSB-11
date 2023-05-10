number = int(input("Input number: "))

total = 0
for digit in str(number):
    total += int(digit)

print(f"Sum of digits of {number} = {total}")

