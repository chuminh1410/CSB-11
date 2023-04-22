import turtle

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def check_right_triangle(a, b, c):
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        return True
    else:
        return False
def check_equilateral_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False
a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))
if check_triangle(a, b, c):
    print("The 3 line segments can form a triangle.")
    if check_right_triangle(a, b, c):
        print("The 3 line segments can form a right triangle.")
    elif check_equilateral_triangle(a, b, c):
        print("The 3 line segments can form an equilateral triangle.")
        t = turtle.Turtle()
        t.color("red")
        t.forward(a)
        t.left(120)
        t.forward(b)
        t.left(120)
        t.forward(c)
        turtle.done()
    else:
        print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")
