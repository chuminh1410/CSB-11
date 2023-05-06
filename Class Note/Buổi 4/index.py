def sum(number):
    total_digits = 0
    digit_sum = 0

    number_str = str(number)

    for char in number_str:
        if char.isdigit():
            total_digits += 1
            digit_sum += int(char)

    return total_digits, digit_sum

number = int(input("Enter yout number: "))
total_digits, digit_sum = sum(number)
print(f"Total digits: {total_digits}")
print(f"Sum of digits: {digit_sum}")