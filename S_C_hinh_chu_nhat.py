color = input ("Nhập màu hoặc mã màu: ")
a = float(input("Nhập chiều dài HCN: "))
b = float(input("Nhập chiều rộng HCN: "))

c = ( a + b ) * 2
s = a * b
print( "Chu vi hình chữ nhật có chiều dài {a} và chiều rộng {b} là: {c}". format (a=a, b=b, c=c))
print( "Diện tích hình chữ nhật có chiều dài {a} và chiều rộng {b} là: {s}". format (a=a, b=b, s=s))

import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(50)
t.color( color )
t.begin_fill()
for i in range(2):
    t.fd(a)
    t.rt(90)
    t.fd(b)
    t.rt(90)
t.end_fill()
turtle.done()