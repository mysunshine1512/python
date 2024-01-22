import turtle
t = turtle.Turtle()

t.penup()
t.goto(200, 100)
t.pendown()

t.pensize(5)
t.pencolor("yellow")

t.fillcolor("yellow")
t.begin_fill()

t.circle(100)
t.end_fill()

turtle.done()
