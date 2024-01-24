import math
R = float(input( "Nhập R: " ))
S = math.pi * R**2
C = 2 * math.pi * R
print ( "Diện tích hình tròn có bán kính {R} là: {S}".format( R = R, S = S))
print ( "Chu vi hình tròn có bán kính {R} là: {C}".format( R = R, C = C))

import turtle
turtle.hideturtle()
turtle.speed(50)
turtle.pencolor("red")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(R)
turtle.end_fill()
turtle.done()