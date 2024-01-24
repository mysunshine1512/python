import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(100)

t.pensize(10)
t.pencolor("yellow")
facesize = 200
t.penup()
t.goto(0, -200)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(facesize)
t.end_fill()
t.penup()

t.pencolor("black")
t.fillcolor("black")
t.penup()
t.goto(-100, 50)
t.pendown()

eye_size = 17.5

t.begin_fill()
t.circle(eye_size)
t.end_fill()
t.penup()

t.goto(100, 50)
t.pendown()
t.begin_fill()
t.circle(eye_size)
t.end_fill()
t.penup()

t.goto(-100, -70)
t.pendown()
t.right(90)
t.circle(100, 180)
turtle.mainloop

turtle.done()