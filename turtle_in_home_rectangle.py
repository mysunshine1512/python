from turtle import *
from random import *
from time import *
hideturtle()
penup()
goto(-380, -280)
pendown()
pensize(5)
speed(100)
pencolor('red')
edge = 0
while edge < 2 :
    fd(760)
    lt(90)
    fd(560)
    lt(90)
    edge += 1
penup()
goto(0, 0)
showturtle()
# hình dạng turtle
shape_set = ((-5, 0), (0, -5), (5, 0), (0, 5))
register_shape('diamond', shape_set)
shape('diamond')
# 
turtlesize(5)
pencolor('green')
fillcolor('green')
hor = randint(-420, 420)
ver = randint(-320, 320)
angle = randint(0, 360)
right(angle)
count = 0
while hor > -380 or hor < 380 or ver > -280 or ver < 280 :
    speed(1)
    hor = randint(-420, 420)
    ver = randint(-320, 320)
    angle = randint(0, 360)
    right(angle)
    goto(hor,ver)
    if hor <= -380 or hor >= 380 or ver <= -280 or ver >= 280 :
        speed(10)
        goto(0, 0)
        count += 1
        if count == 2 :
            break
        hideturtle()
        goto(-320, 320)
        write('Sao kỳ dzậy má, đi hông được à???', font=('arial', 31))
        goto(0, 0)
        showturtle()
hideturtle()
goto(-180, 30)
write('Mệt tóa @@\nChính thức bỏ cuộc!\nHông đi nữa đâu T_T', font=('arial', 31))
home()
showturtle()
sleep(3)
# done()
