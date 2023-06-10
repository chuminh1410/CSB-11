import turtle
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

t = turtle.Turtle()
for color in color_list:
    t.pencolor(color)
    t.forward(50)
turtle.done()
