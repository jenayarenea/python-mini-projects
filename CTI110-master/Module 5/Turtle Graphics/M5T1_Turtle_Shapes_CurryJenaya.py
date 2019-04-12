#CTI 110
#M5T1 Turtle Shapes
#Jenaya Curry
#24 October 2017
#This program draws a square and a triangle in turtle graphics.

def mainSquare():
    import turtle
    turtle.pencolor('purple')
    turtle.shape("turtle")
    i=0
    while i<4:
        turtle.forward(125)
        turtle.left(90)
        i=i+1
    mainTriangle()

def mainTriangle():
    import turtle
    turtle.pencolor('yellow')
    turtle.shape('turtle')
    s=0
    while s<3:
        turtle.forward(100)
        turtle.left(120)
        s=s+1
    turtle.exitonclick()

mainSquare()

