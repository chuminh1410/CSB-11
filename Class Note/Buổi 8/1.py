def calculate_sum(*args):
    return sum(args)

nums = input("Enter a list of numbers separated by spaces: ").split()

args = [int(num) for num in nums]

result = calculate_sum(*args)
print("Sum:", result)
