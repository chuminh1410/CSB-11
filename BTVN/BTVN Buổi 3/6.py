print("Please enter the lengths of three line segments:")
a = float(input("Length of segment 1: "))
b = float(input("Length of segment 2: "))
c = float(input("Length of segment 3: "))

if a + b > c and a + c > b and b + c > a:
    print("The three line segments can form a triangle.")
else:
    print("The three line segments cannot form a triangle.")
