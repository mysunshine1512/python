from turtle import *
from random import *
from time import *
hideturtle()
penup()
goto(0, -350)
pendown()
pensize(5)
speed(100)
pencolor('red')
circle(350)
penup()
goto(0, 0)
shape('turtle')
showturtle()
turtlesize(2.5)
pencolor('green')
fillcolor('green')
angle = randint(0, 360)
right(angle)
count = 0
range = 0
while range < 350 :
    speed(1)
    d = randint(1,100)
    forward(d)
    range += d
    if range >= 350 :
        speed(10)
        goto(0, 0)
        range = 0
        angle = randint(0, 360)
        right(angle)
        count += 1
        if count == 5 :
            break
        hideturtle()
        goto(-240, 350)
        write('Cho em đi chơi đi mà T_T', font=('arial', 31))
        goto(0, 0)
        showturtle()
hideturtle()
goto(-180, 30)
write('Mệt tóa @@\nChính thức bỏ cuộc!\nHông đi nữa đâu T_T', font=('arial', 31))
home()
showturtle()
sleep(3)
# done()