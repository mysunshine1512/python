a = int(input("Nhập chiều dài cạnh hình vuông: "))
from turtle import *
hideturtle()
pencolor("aqua")
edge = 0
while edge < 4 :
    fd(a)
    rt(90)
    edge += 1
done()
