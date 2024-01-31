from turtle import *
from random import *
def elip1(size, col) :
    '''Hàm vẽ hình elip có độ lớn là size.
        Cú pháp là: elip( size )
        Dấu + và - trước size thể hiện chiều vẽ.'''
    pendown()
    begin_fill()
    pencolor(col)
    fillcolor(col)
    for i in range(2) :
        circle(size, 25)
        circle(size / 8, 130)
        circle(size, 25)
    end_fill()
    penup()

def elip2(size, col) :
    '''Hàm vẽ hình elip có độ lớn là size.
        Cú pháp là: elip( size )
        Dấu + và - trước size thể hiện chiều vẽ.'''
    pendown()
    begin_fill()
    pencolor(col)
    fillcolor(col)
    for i in range(2) :
        circle(size, 20)
        circle(size / 10, 140)
        circle(size, 20)
    end_fill()
    penup()

def cloud1(size, col) :
    for i in range(2) :
        begin_fill()
        pencolor(col)
        fillcolor(col)
        # elip
        pendown()
        for i in range(2) :
            circle(size, 25)
            circle(size / 8, 130)
            circle(size, 25)
        penup()
        # 
        end_fill()
        fd(size * 175/200)
        lt(90)
        fd(size * 25/200)
        rt(90)
        begin_fill()
        pencolor(col)
        fillcolor(col)
        # elip
        pendown()
        for i in range(2) :
            circle(size, 25)
            circle(size / 8, 130)
            circle(size, 25)
        penup()
        # 
        end_fill()
        lt(90)
        fd(size * 125/200)
        lt(90)
        fd(size * 110/200)
def cloud2(size, col) :
    for i in range(2) :
        begin_fill()
        pencolor(col)
        fillcolor(col)
        # elip
        pendown()
        for i in range(2) :
            circle(size, 20)
            circle(size / 10, 140)
            circle(size, 20)
        penup()
        # 
        end_fill()
        bk(size * 130/200)
        rt(90)
        bk(size * 20/200)
        lt(90)
        begin_fill()
        pencolor(col)
        fillcolor(col)
        # elip
        pendown()
        for i in range(2) :
            circle(size, 20)
            circle(size / 10, 140)
            circle(size, 20)
        penup()
        # 
        end_fill()
        rt(90)
        bk(size * 90/200)
        rt(90)
        bk(size * 80/200)

# Thử nghiệm
def lineup(x, y, col) :
    goto(x, y)
    color(col)
    pendown()
    begin_fill()
    while distance((x, y), pos()) < 1000 :
        lt(25)
        d = randint(10,30)
        forward(d)
        rt(26)
        d = randint(15,40)
        forward(d)
        if distance((x, y), pos()) >= 1000 :
            goto((500, 500))
            goto((-500, 500))
            goto(x, y)
            penup()
            home()
            break
    end_fill()

def linedown(x, y, col) :
    goto(x, y)
    color(col)
    pendown()
    begin_fill()
    while distance((x, y), pos()) < 1000 :
        rt(25)
        d = randint(10,30)
        forward(d)
        lt(26)
        d = randint(15,40)
        forward(d)
        if distance((x, y), pos()) >= 1000 :
            goto((500, -500))
            goto((-500, -500))
            goto(x, y)
            penup()
            home()
            break
    end_fill()