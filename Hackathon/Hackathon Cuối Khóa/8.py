def fibonacci_sequence(n):
    sequence = []
    if n >= 1:
        sequence.append(1)
    if n >= 2:
        sequence.append(1)

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence

n = int(input("Input a positive number: "))

fibonacci_numbers = fibonacci_sequence(n)
print(f"First {n} Fibonacci number(s):")
for number in fibonacci_numbers:
    print(number, end=" ")
