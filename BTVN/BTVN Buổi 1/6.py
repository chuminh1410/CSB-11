import turtle

t = turtle.Turtle()

t.pensize(4)
for i in range(4):
    t.forward(200)
    t.left(90)

t.penup()
t.goto(10,10)  
t.pendown()
t.pensize(2)
for i in range(4):
    t.forward(180)
    t.left(90)

turtle.done()
