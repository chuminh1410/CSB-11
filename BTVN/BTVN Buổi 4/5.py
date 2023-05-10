count = 0
number = 1000

print("Numbers with sum of digits = 9:")

while count < 10:
    digit_sum = sum(int(digit) for digit in str(number))
    if digit_sum == 9:
        print(number, end=" ")
        count += 1
    number += 1
