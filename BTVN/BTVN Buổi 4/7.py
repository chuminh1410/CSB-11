import turtle

radius = 10
angle = 90
increment = 5

turtle.speed(10)

while radius < 300:
    turtle.circle(radius, angle)
    radius += increment

turtle.done()

