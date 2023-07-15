import math

def quadratic_equation(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "The equation has no real solutiuon"
    elif delta == 0:
        x = -b / (2*a)
        return f"The equation has one double solution, x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"The equation has two solution, x1 = {x1}, x2 = {x2}"

a = int(input("Input a: "))

condition = True
while condition == True:
    if a == 0:
        a = int(input("a cannot be 0: "))
    else:
        condition =False
        
b = int(input("Input b: "))
c = int(input("Input c: "))

result = quadratic_equation(a,b,c)
print(result)