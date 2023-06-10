def reverse(text):
    reversed_text = text[::-1]
    return reversed_text

text = input("Input a text: ")
reversed_text = reverse(text)
print("Reversed text:", reversed_text)
