numbers = []
num = int(input("Input the list of numbers.\nEnter 0 to finish.\n"))

while num != 0:
    numbers.append(num)
    num = int(input())

total = sum(numbers)
print("Sum of numbers in list:", total)
