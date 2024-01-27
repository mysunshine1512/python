from turtle import *
from random import *
# setup
hideturtle()
pensize(5)
penup()
goto(-400, 0)
showturtle()
range = 0
while range < 800:
    down = randint(10, 30)
    up = randint(10, 30)
    pendown()
    forward(down)
    penup()
    forward(up)
    range += down + up
done()