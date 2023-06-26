sequence = input("Input sequence: ")

frequency = {}
for char in sequence:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Frequency of characters:")
print(frequency)
