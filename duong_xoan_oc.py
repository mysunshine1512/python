from turtle import *
from math import *
from time import *
title('Rùa chạy xoắn ốc')
shape('turtle')
turtlesize(1)
pencolor('green')
fillcolor('green')
d = 0.5
while distance((0, 0), pos()) < 300 :
    speed(1)
    forward(d)
    rt(10)
    d += 0.25
    if distance((0, 0), pos()) >= 300 :
        break

sleep(3)