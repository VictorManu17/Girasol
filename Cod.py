import math
import turtle

# Configuración inicial
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

# El tallo
turtle.penup()
turtle.goto(10, -500)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green")  # Color del tallo
turtle.begin_fill()
turtle.forward(500)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(500)
turtle.end_fill()

# Color del centro del girasol
turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("#8B4513")  # Café claro
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Código del girasol
phi=137.508 *(math.pi/180.0)
for i in range (160+40):
    r=4*math.sqrt(i)
    theta=i*phi
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(i*137.508)
    turtle.pendown()
    if i<160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()
    turtle.hideturtle()

turtle.penup()
turtle.goto(0,400)
turtle.color("white")
turtle.write("ESCRIBE SI QUIERES UN MENSAJE", align="center", font=("times new roman",24,"bold"))

turtle.exitonclick()