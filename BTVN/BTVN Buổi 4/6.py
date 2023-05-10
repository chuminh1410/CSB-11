import turtle as t 

edges = int(input("Input number of edges: "))

if edges < 3:
    print("Invalid number of edges.")

angle = 360 / edges

window = t.Screen()
t.speed(1)

for i in range(edges):
    t.forward(100)
    t.right(angle)

t.done()