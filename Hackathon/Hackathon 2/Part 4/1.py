numbers = [5, 1, 8, 92, 7, 30]

even_num = []

for num in numbers:
    if num % 2 == 0:
        even_num.append(num)

print("Even numbers:", ", ".join(map(str, even_num)))