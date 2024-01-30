from turtle import *
from random import *
def rectangle_af(x, y, col) :
    color(col)
    pensize(1)
    begin_fill()
    pendown()
    for i in range(2) :
        fd(x)
        lt(90)
        fd(y)
        lt(90)
    end_fill()
    penup()

def rectangle_1_fd(x, y, again, col) :
    for i in range(again) :
        pensize(1)
        color(col)
        begin_fill()
        pendown()
        for j in range(2) :
            fd(x)
            lt(90)
            fd(y)
            lt(90)
        end_fill()
        penup()
        lt(90)
        fd(y)
        rt(90)
    rt(90)
    fd((i + 1) * y)
    lt(90)

def rectangle_2_fd(x, y, x_ratio, y_ratio, again, col1, col2) :
    for i in range(again) :
        pensize(1)
        color(col1)
        begin_fill()
        pendown()
        for j in range(2) :
            fd(x)
            lt(90)
            fd(y)
            lt(90)
        end_fill()
        penup()
        fd(x * ((100 - x_ratio)/2)/100)
        lt(90)
        fd(y * ((100 - y_ratio)/2)/100)
        rt(90)
        color(col2)
        begin_fill()
        pendown()
        for j in range(2) :
            fd(x * x_ratio/100)
            lt(90)
            fd(y * y_ratio/100)
            lt(90)
        end_fill()
        penup()
        bk(x * ((100 - x_ratio)/2)/100)
        lt(90)
        bk(y * ((100 - y_ratio)/2)/100)
        fd(y)
        rt(90)
    rt(90)
    fd((i + 1) * y)
    lt(90)

def rectangle_rd_fd(x, y, x_ratio, y_ratio, again, col, col_random_1, col_random_2) :
    for i in range(again) :
        pensize(1)
        color(col)
        begin_fill()
        pendown()
        for j in range(2) :
            fd(x)
            lt(90)
            fd(y)
            lt(90)
        end_fill()
        penup()
        fd(x * ((100 - x_ratio)/2)/100)
        lt(90)
        fd(y * ((100 - y_ratio)/2)/100)
        rt(90)
        rcol = { 1 : col_random_1 , 2 : col_random_2 , 3 : col_random_2 , 4 : col_random_2 , 5 : col_random_2 , \
                 6 : col_random_2 , 7 : col_random_2 , 8 : col_random_2 , 9 : col_random_2 , 10 : col_random_2 }
        a = randint(1, 10)
        color(rcol[a])
        begin_fill()
        pendown()
        for j in range(2) :
            fd(x * x_ratio/100)
            lt(90)
            fd(y * y_ratio/100)
            lt(90)
        end_fill()
        penup()
        bk(x * ((100 - x_ratio)/2)/100)
        lt(90)
        bk(y * ((100 - y_ratio)/2)/100)
        fd(y)
        rt(90)
    rt(90)
    fd((i + 1) * y)
    lt(90)
