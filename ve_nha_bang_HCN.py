from turtle import *
from random import *
from rectangle_forward import *
from sky_cloud import *
hideturtle()
bgcolor('#025F81')
hideturtle()
speed(0)
penup()
# nền trời
linedown(-500, 30, '#357E9F')
linedown(-500, -50, '#40819F')
lineup(-500, -90, '#025F81')
lineup(-500, 35, '#065C7F')
lineup(-500, 170, '#00496C')  
lineup(-500, 250, '#014363')
lineup(-500, 300, '#003350')

# mây
goto(-200, -50)
cloud2(100, '#8096A1')
goto(-320,-30)
elip2(60, '#8096A1')

goto(-400, 40)
cloud2(100, '#668A9A')
goto(-315,60)
elip2(50, '#668A9A')
goto(-295,65)
elip2(30, '#668A9A')

goto(-380, 110)
cloud1(130, '#5C7F92')

goto(150, 45)
cloud1(180, '#3C7388')
goto(390, 90)
elip1(100, '#3C7388')

goto(-100, 50)
cloud1(100, '#548498')
goto(45, 77)
elip1(50, '#548498')

goto(380, 100)
cloud2(170, '#3F7B95')
goto(190, 130)
elip1(75, '#3F7B95')

# nhà
# dãy sau cùng
# 1
goto(-430, -250)
for i in range(1) :
    rectangle_rd_fd(14, 18, 80, 80, 10, '#3E4150', '#EFCFB8', '#142535')
    fd(14)
for i in range(6) :
    rectangle_rd_fd(14, 18, 80, 80, 11, '#3E4150', '#EFCFB8', '#142535')
    fd(14)
for i in range(1) :
    rectangle_rd_fd(14, 18, 80, 80, 10, '#3E4150', '#EFCFB8', '#142535')
    fd(14)
# 2
goto(-300, -400)
rectangle_af(80, 120, '#435B73')
fd(10)
rectangle_af(60, 130, '#435B73') 
rectangle_af(60, 110, '#22445F')
fd(20)
lt(90)
fd(90)
rectangle_af(5, 5, '#E7F9FD')
fd(10)
rt(90)
fd(10)
rectangle_af(5, 5, '#E7F9FD')
fd(10)
rt(90)
fd(30)
rectangle_af(5, 5, '#E7F9FD')
lt(90)
# 3
goto(180, -400)
rectangle_af(120, 140, '#435B73')
fd(20)
rectangle_af(80, 150, '#435B73') 
rectangle_af(80, 120, '#22445F')
lt(90)
fd(90)
rectangle_af(5, 5, '#E7F9FD')
fd(15)
rt(90)
fd(10)
rectangle_af(10, 10, '#E7F9FD')
fd(10)
rt(90)
fd(30)
rectangle_af(10, 10, '#E7F9FD')
lt(90)

# dãy trước 1 chút
# 1
goto(-410, -400)
rectangle_af(110, 220, '#0A2538')
goto(-430, -400)
rectangle_af(90, 200, '#383F51')
fd(15)
rectangle_rd_fd(20, 25, 70, 50, 8, '#383F51', '#EEE1B7', '#13161F' )
fd(40)
rectangle_rd_fd(20, 25, 70, 50, 8, '#383F51', '#EEE1B7', '#13161F' )
fd(35)
rectangle_af(60, 200, '#1E263B')
fd(20)
rectangle_rd_fd(20, 25, 70, 50, 8, '#1E263B', '#EEE1B7', '#13161F' )
# 2
# mái
goto(270, -170)
rectangle_af(-15, 5, '#152233')
rectangle_af(150, 5, '#152233')
rectangle_af(135, 10, '#152233')
# nhà
goto(240, -400)
rectangle_af(195, 230, '#4B4B57')
fd(5)
rectangle_rd_fd(20, 28, 70, 50, 8, '#4B4B57', '#FFECDA', '#09111C' )
fd(30)
rectangle_rd_fd(20, 28, 70, 50, 8, '#4B4B57', '#FFECDA', '#09111C' )
fd(30)
rectangle_rd_fd(20, 28, 70, 50, 8, '#4B4B57', '#FFECDA', '#09111C' )
fd(25)
rectangle_af(105, 230, '#343B4B')
fd(5)
rectangle_rd_fd(20, 28, 20, 20, 8, '#343B4B', '#FFECDA', '#09111C' )
fd(25)
rectangle_rd_fd(20, 28, 70, 50, 8, '#343B4B', '#FFECDA', '#09111C' )
fd(25)
rectangle_rd_fd(20, 28, 70, 50, 8, '#343B4B', '#FFECDA', '#09111C' )
fd(25)
rectangle_rd_fd(20, 28, 20, 20, 8, '#343B4B', '#FFECDA', '#09111C' )

# dãy trước 1 chút nữa
# 1
goto(-230, -400)
rectangle_af(3, 18 * 19, '#1B2733')
fd(3)
# mái 1
lt(90)
fd(18 * 19 + 5)
rt(90)
rectangle_af(15 * 2 + 5 * 2 + 14 * 11 , - 5, '#D3AC8F')
rectangle_af(15 * 2 + 14 * 3 , - 18 * 2 - 5, '#666273')
rectangle_af(15 * 2 + 14 * 3 , - 18 * 1.5 - 5, '#1B2733')
fd(10)
rectangle_af((15 * 2 + 5 * 2 + 14 * 11) - 10 * 2, 18 * 1, '#90665A')
rectangle_af((15 * 2 + 14 * 3) - 10 * 2 , 18 * 1, '#666273')
fd(10)
lt(90)
fd(18)
rt(90)
rectangle_af((15 * 2 + 5 * 2 + 14 * 11) - 10 * 4, 18 * 1, '#AE9C90')
rectangle_af((15 * 2 + 14 * 3) - 10 * 4 , 18 * 1, '#666273')
bk(20)
rt(90)
fd(18 * 20 + 5)
lt(90)
# 
rectangle_af(15, 18 * 17, '#666273')
fd(15)
for i in range(3) :
    rectangle_rd_fd(14, 18, 80, 80, 17, '#3E4150', '#EFCFB8', '#142535')
    fd(14)
rectangle_af(15, 18 * 17, '#666273')
fd(15)
rectangle_af(5, 18 * 19, '#1B2733')
fd(5)
for i in range(3) :
    rectangle_rd_fd(14, 18, 80, 80, 19, '#D3AC8F', '#FFDBB7', '#331713')
    fd(14)
rectangle_af(5, 18 * 19, '#1B2733')
fd(5)
for i in range(2) :
    rectangle_rd_fd(14, 18, 80, 80, 19, '#D3AC8F', '#FFDBB7', '#331713')
    fd(14)
rectangle_af(5, 18 * 19, '#1B2733')
fd(5)
for i in range(3) :
    rectangle_rd_fd(14, 18, 80, 80, 19, '#D3AC8F', '#FFDBB7', '#331713')
    fd(14)

# 2
goto(30, -400)
for i in range(3) :
    rectangle_rd_fd(14, 18, 80, 80, 17, '#D3AC8F', '#FFDBB7', '#331713')
    fd(14)
rectangle_af(5, 18 * 17, '#1B2733')
fd(5)
for i in range(3) :
    rectangle_rd_fd(14, 18, 80, 80, 17, '#D3AC8F', '#FFDBB7', '#331713')
    fd(14)
rectangle_af(5, 18 * 17, '#1B2733')
fd(5)
rectangle_af(15, 18 * 17, '#666273')
fd(15)
for i in range(4) :
    rectangle_rd_fd(14, 18, 80, 80, 15, '#3E4150', '#EFCFB8', '#142535')
    fd(14)
rectangle_af(15, 18 * 15, '#666273')
fd(15)
# mái 2
lt(90)
fd(18 * 17 + 5)
rt(90)
rectangle_af( - (15 * 2 + 5 * 1 + 14 * 10) , - 5, '#D3AC8F')
rectangle_af( - (15 * 2 + 14 * 4) , - 18 * 2 - 5, '#666273')
rectangle_af( - (15 * 2 + 14 * 4) , - 18 * 1.5 - 5, '#1B2733')
bk(10)
rectangle_af( - ((15 * 2 + 5 * 1 + 14 * 10) - 10 * 2), 18 * 1, '#90665A')
rectangle_af( - ((15 * 2 + 14 * 4) - 10 * 2) , 18 * 1, '#666273')
bk(10)
lt(90)
fd(18)
rt(90)
rectangle_af( - ((15 * 2 + 5 * 1 + 14 * 10) - 10 * 4), 18 * 1, '#AE9C90')
rectangle_af( - ((15 * 2 + 14 * 4) - 10 * 4) , 18 * 1, '#666273')
fd(20)
rt(90)
fd(18 * 18 + 5)
lt(90)
# 
rectangle_af(5, 18 * 17, '#1B2733')
fd(3)

# nhà trung tâm
# khung
goto(-95, -400)
rectangle_af(129 + 60, 70, '#564742')
goto(-75.5, -330)
rt(90)
rectangle_2_fd(70, 30, 65, 75, 5, '#564742', '#F6FFEC')
lt(90)
# 1
goto(-95, -330)
rectangle_af(189, 35, '#42352D')
# 2
fd(15)
rectangle_af(159, 110, '#42352D')
# 3
fd(16)
rectangle_af(127, 391, '#42352D')
rectangle_af(111, 403, '#42352D')
# 4
fd(16)
rectangle_af(95, 535, '#42352D')
fd(16)
rectangle_af(79, 560, '#42352D')
# 5
lt(90)
fd(560)
rt(90)
rectangle_af(62, 20, '#041A28')
# 6
fd(18)
rectangle_af(26, 131, '#041A28')
# chóp
fd(11)
rectangle_af(4, 159, '#F0F4F5')
rectangle_af(4, 155, '#041A28')
goto(-14, 231)
for i in range(2) :
    rectangle_2_fd(13, 13, 50, 50, 10, '#041A28', '#F0F4F5')
    fd(13)

# tia sáng
goto(-95, -330)
# 1
for i in range(5) : 
    rectangle_af(1, 35, '#FFE6BA')
    fd(3)
fd(1)
# 2
for i in range(5) : 
    rectangle_af(1, 110, '#FFE6BA')
    fd(3)
fd(1)
# 3 4
for i in range(2) :
    for i in range(2) : 
        rectangle_af(1, 305, '#FFE6BA')
        fd(3)
        rectangle_af(1, 375, '#FFE6BA')
        fd(3)
    rectangle_af(1, 305, '#FFE6BA')    
    fd(4)
# 5
for i in range(2) : 
    rectangle_af(1, 175, '#FFE6BA')
    fd(3)
    rectangle_af(1, 375, '#FFE6BA')
    fd(3)
rectangle_af(1, 175, '#FFE6BA')    
fd(4)
# 6 7
for i in range(2) : 
    for i in range(5) : 
        rectangle_af(1, 375, '#FFE6BA')
        fd(3)
    fd(1)
# 8
for i in range(2) : 
    rectangle_af(1, 175, '#FFE6BA')
    fd(3)
    rectangle_af(1, 375, '#FFE6BA')
    fd(3)
rectangle_af(1, 175, '#FFE6BA')    
fd(4)
# 9 10
for i in range(2) :
    for i in range(2) : 
        rectangle_af(1, 285, '#FFE6BA')
        fd(3)
        rectangle_af(1, 375, '#FFE6BA')
        fd(3)
    rectangle_af(1, 285, '#FFE6BA')    
    fd(4)
# 11
for i in range(5) : 
    rectangle_af(1, 110, '#FFE6BA')
    fd(3)
fd(1)
# 12
for i in range(5) : 
    rectangle_af(1, 35, '#FFE6BA')
    fd(3)
fd(1)
# ngấn
goto(-16, -260)
rectangle_af(32, 2, '#764525')
# ô nhà
goto(-63, 46)
for i in range(2) :
    rectangle_2_fd(8, 12, 50, 50, 2, '#42352D', '#FFE6BA')
    fd(9)
for i in range(2) :
    rectangle_2_fd(8, 12, 50, 50, 13, '#42352D', '#FFE6BA')
    fd(9)
for i in range(8) :
    rectangle_2_fd(8, 12, 50, 50, 15, '#42352D', '#FFE6BA')
    fd(9)
for i in range(2) :
    rectangle_2_fd(8, 12, 50, 50, 1, '#42352D', '#FFE6BA')
    fd(9)

done()