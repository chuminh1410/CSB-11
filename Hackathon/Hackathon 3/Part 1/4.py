def palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

text = input("Enter a string: ")

if palindrome(text):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
