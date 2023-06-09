def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Input number: "))

count = 0
number = 2
primes = []

while count < n:
    if is_prime(number):
        primes.append(number)
        count += 1
    number += 1

print(f"First {n} prime(s): {' '.join(map(str, primes))}")
