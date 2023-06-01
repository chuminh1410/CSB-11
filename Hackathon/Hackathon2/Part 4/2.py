numbers = []
num = int(input("Input the list of numbers.\nEnter 0 to finish.\n"))

while num != 0:
    numbers.append(num)
    num = int(input())

even_num = []

for num in numbers:
    if num % 2 == 0:
        even_num.append(num)

print("Even numbers:", ", ".join(map(str, even_num)))
