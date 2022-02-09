from turtle import Turtle, Screen, Pen

sc = Screen()
tam = Turtle()
sc.setup(width=1200, height=700)
tam.shape("turtle")
tam.pen(fillcolor="black", pencolor="red", pensize=10)
tam.penup()
tam.left(180)
tam.forward(420)
tam.right(90)
tam.forward(300)
tam.right(90)
tam.forward(60)
tam.left(180)

tam.speed(1)
# c
tam.pendown()
tam.circle(100, 180)

tam.penup()
tam.forward(50)

# a
tam.pendown()
tam.left(70)
tam.forward(190)
tam.right(140)
tam.forward(190)
tam.penup()
tam.left(180)
tam.forward(190/2)
tam.pendown()
tam.left(70)
tam.forward(70)

tam.penup()
tam.left(90)
tam.forward(190/2)
tam.left(90)
tam.forward(150)

# r
tam.pendown()
tam.left(90)
tam.forward(200)
tam.right(90)
for x in range(180):
    tam.right(1)
    tam.forward(1.3)
tam.left(140)
tam.forward(190/2)

tam.penup()
tam.left(40)
tam.forward(70)

# m
tam.pendown()
tam.left(90)
tam.forward(200)
tam.right(145)
tam.forward(100)
tam.left(110)
tam.forward(100)
tam.right(145)
tam.forward(200)


tam.penup()
tam.left(90)
tam.forward(70)

# e
tam.left(90)
tam.forward(200)
tam.pendown()
tam.left(180)
tam.forward(200)
tam.left(90)
tam.forward(70)
tam.penup()
tam.left(90)
tam.forward(100)
tam.pendown()
tam.left(90)
tam.forward(70)
tam.penup()
tam.right(90)
tam.forward(100)
tam.pendown()
tam.right(90)
tam.forward(70)

tam.penup()
tam.forward(40)
tam.right(90)
tam.forward(200)
tam.left(180)

# n
tam.pendown()
tam.forward(200)
tam.right(150)
tam.forward(230)
tam.left(150)
tam.forward(200)

sc.exitonclick()



