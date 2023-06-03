def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

text = input("Enter a string: ")
upper, lower = count_upper_lower(text)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
