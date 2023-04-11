import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(200)
    t.left(90)
t.left(90)
t.forward(100)
t.right(90)
t.penup()
t.forward(200)
t.forward(40)
t.pendown()
t.left(90)
t.left(45)
for i in range(4):
    t.forward(200)
    t.left(90)

turtle.done()
