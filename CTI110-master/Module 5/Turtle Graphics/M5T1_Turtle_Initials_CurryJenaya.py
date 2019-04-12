#CTI 110
#M5T1 Turtle Initials
#Jenaya Curry
#24 October 2017
#This program draws the intials 'JC' in turtle graphics.

def mainInitials():
    import turtle
    turtle.pencolor('purple')
    turtle.shape('turtle')
    turtle.pensize(13)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(75)
    turtle.exitonclick()

mainInitials()
