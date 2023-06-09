def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_expression(n):
    result = 0
    for i in range(1, n + 1):
        result += factorial(i) / i
    return result

n = int(input("Input number: "))
result = calculate_expression(n)
print("Result:", result)

