import turtle
t = turtle.Turtle()
t.speed(10)
t.hideturtle()
turtle.bgcolor("#6895D2")
t.penup()

t.goto(0, -110)
t.pendown()
t.pencolor("#967E76")
t.fillcolor("#967E76")
t.begin_fill()
t.fd(500)
t.rt(90)
t.fd(500)
t.rt(90)
t.fd(1000)
t.rt(90)
t.fd(500)
t.rt(90)
t.fd(500)
t.end_fill()
t.penup()

# mặt trời
# tia
t.pensize(10)
t.pencolor("#D04848")
for i in range(8):
    t.goto(100, 250)
    t.pendown()
    t.fd(100)
    t.penup()
    t.goto(100, 250)
    t.lt(22.5)
    t.pendown()
    t.fd(75)
    t.penup()
    t.lt(22.5)

# hình tròn
t.pencolor("#FDE767")
t.goto(100, 250)
t.dot(100)
t.penup()

# ngôi nhà
t.pensize(1)
t.pencolor("#F8FAE5")
t.fillcolor("#F8FAE5")
t.begin_fill()
t.goto(-75, -100)
t.pendown()
t.goto(-275, -100)
t.goto(-275, -200)
t.goto(-75, -200)
t.goto(-75, -100)
t.end_fill()
# mái
t.pencolor("#76453B")
t.fillcolor("#76453B")
t.begin_fill()
t.goto(-25, -100)
t.goto(-100, -50)
t.goto(-250, -50)
t.goto(-325, -100)
t.goto(-75, -100)
t.end_fill()
t.penup()
# nhà 2
t.pencolor("#F8FAE5")
t.fillcolor("#F8FAE5")
t.begin_fill()
t.goto(-125, 25)
t.pendown()
t.goto(-125, -50)
t.goto(-225, -50)
t.goto(-225, 25)
t.goto(-125, 25)
t.end_fill()
# mái 2
t.pencolor("#76453B")
t.fillcolor("#76453B")
t.begin_fill()
t.goto(-100, 25)
t.goto(-150, 55)
t.goto(-200, 55)
t.goto(-250, 25)
t.goto(-125, 25)
t.end_fill()
t.penup()
# nhà đỉnh
t.pencolor("#F8FAE5")
t.fillcolor("#F8FAE5")
t.begin_fill()
t.goto(-200, 75)
t.pendown()
t.goto(-200, 55)
t.goto(-150, 55)
t.goto(-150, 75)

# mái đỉnh
t.pensize(5)
t.pencolor("#76453B")
t.goto(-175, 95)
t.goto(-200, 75)

t.pensize(1)
t.pencolor("#F8FAE5")
t.end_fill()
t.penup()

# cửa
# cửa 1
t.pencolor("#76453B")
t.goto(-175, -150)
t.dot(52)
t.pencolor("black")
t.fillcolor("#76453B")
t.begin_fill()
t.pendown()
t.goto(-200, -150)
t.goto(-200, -200)
t.goto(-150, -200)
t.goto(-150, -150)
t.goto(-175, -150)
t.goto(-175, -200)
t.end_fill()
t.penup()
# cửa sổ phải
t.pencolor("#76453B")
t.goto(-112.5, -165)
t.dot(26)
t.pencolor("black")
t.fillcolor("#76453B")
t.begin_fill()
t.pendown()
t.goto(-125, -165)
t.goto(-125, -190)
t.goto(-99.5, -190)
t.goto(-99.5, -165)
t.goto(-112.5, -165)
t.goto(-112.5, -190)
t.end_fill()
t.penup()
# cửa sổ trái
t.pencolor("#76453B")
t.goto(-237.5, -165)
t.dot(26)
t.pencolor("black")
t.fillcolor("#76453B")
t.begin_fill()
t.pendown()
t.goto(-250, -165)
t.goto(-250, -190)
t.goto(-224.5, -190)
t.goto(-224.5, -165)
t.goto(-237.5, -165)
t.goto(-237.5, -190)
t.end_fill()
t.penup()
# cửa 2
t.goto(-175, -50)
t.pencolor("black")
t.fillcolor("#76453B")
t.begin_fill()
t.pendown()
t.goto(-195, -50)
t.goto(-195, 0)
t.goto(-155,0)
t.goto(-155, -50)
t.goto(-175, -50)
t.goto(-175, 0)
t.end_fill()
t.penup()
# cửa 3
t.goto(-175, 65)
t.pencolor("#76453B")
t.begin_fill()
t.dot(12)

# cây
# thân cây
t.pencolor("#665A48")
t.fillcolor("#665A48")
t.goto(200, -200)
t.begin_fill()
t.pendown()
t.goto(225, -200)
t.goto(220, -75)
t.goto(275, 0)
t.goto(212.5, -60)
t.goto(125, 0)
t.goto(205, -75)
t.goto(200, -200)
t.end_fill()
t.penup()

# tán cây
t.goto(210, 60)
t.pencolor("#A4BE7B")
t.dot(150)

t.goto(270, 0)
t.pencolor("#5F8D4E")
t.dot(125)

t.goto(150, -25)
t.pencolor("#285430")
t.dot(135)

# mây
t.pencolor("#FFFBF5")
t.fillcolor("#FFFBF5")
t.goto(-50, 200)
t.begin_fill()
t.pendown()
t.circle(12, 180)
t.fd(250)
t.circle(12, 180)
t.fd(250)
t.end_fill()
t.penup()

t.goto(-50, 240)
t.dot(55)

t.goto(-100, 275)
t.dot(115)

t.goto(-160, 250)
t.dot(90)

t.goto(-240, 280)
t.dot(140)

t.goto(-300, 240)
t.dot(60)

turtle.done()