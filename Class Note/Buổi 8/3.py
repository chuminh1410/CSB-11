def palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

text = input("Enter a string: ")

if palindrome(text):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")
