from turtle import *
from random import *
number = int(uniform(0, 7))

bgcolor("black")
title("Màu của quả bóng")
shape("circle")
if number < 1 :
    color("red")
elif number < 2 :
    color("orange")
elif number < 3 :
    color("yellow")
elif number < 4 :
    color("green")
elif number < 5 :
    color("blue")
elif number < 6 :
    color("indigo")
elif number < 7 :
    color("violet")
else :
    color("white")
done()

