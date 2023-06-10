def odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Input a number: "))

if odd(num):
    print("This number is even")
else:
    print("This number is not even")