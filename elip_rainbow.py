from turtle import *
n = 1
while n < 37 :
    if  n % 12 == 1 :
        color('#DF0029')
    elif n % 12 == 2 :
        color('#E33539')
    elif n % 12 == 3 :
        color('#EC870E')
    elif n % 12 == 4 :
        color('#F1AF00')
    elif n % 12 == 5 :
        color('#F9F400')
    elif n % 12 == 6 :
        color('#5BBD2B')
    elif n % 12 == 7 :
        color('#00A06B')
    elif n % 12 == 8 :
        color('#00A6AD')
    elif n % 12 == 9 :
        color('#205AA7')
    elif n % 12 == 10 :
        color('#3A2885')
    elif n % 12 == 11 :
        color('#5D0C7B')
    else :
        color('#A2007C')
    general = 0
    bgcolor('black')
    speed(1000)
    hideturtle()
    pensize(2)
    rt(10)
    while general <2 :
        pencolor = color
        circle(200, 90)
        circle(100, 90)
        general += 1
    n += 1
    if n >= 37 :
        break
done()