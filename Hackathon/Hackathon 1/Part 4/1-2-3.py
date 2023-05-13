def is_valid_email(email):
    if "@" in email and "." in email[email.index("@"):]:
        return True
    return False

print("== Registration ==")
username = input("Username: ")

valid_password = False
while not valid_password:
    password = input("Password: ")
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        valid_password = True
    else:
        print("Invalid password. Please input again.")

repeat_password = input("Repeat password: ")

valid_email = False
while not valid_email:
    email = input("Email: ")
    if is_valid_email(email):
        valid_email = True
    else:
        print("Invalid email. Please input again.")

if password == repeat_password and username and valid_password and valid_email:
    print("Registered successfully.")
else:
    print("Invalid registration information.")
