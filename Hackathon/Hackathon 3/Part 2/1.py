import math

def factorial(num):
    num_fac = math.factorial(num)
    return num_fac

num = int(input("Input a number: "))

num_fac = factorial(num)
print(str(num) + "! = " + str(num_fac))
