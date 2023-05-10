import turtle

edges = int(input("Input number of edges: "))

if edges < 3:
    print("Invalid number of edges.")

angle = 360 / edges

window = turtle.Screen()
turtle.speed(1)

for i in range(edges):
    turtle.forward(100)
    turtle.right(angle)

turtle.done()