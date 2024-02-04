from turtle import *
from random import *
from time import *
penup()
hideturtle()

# Setup ban đầu
WIDTH = 900
HEIGHT = 610
white = '#FFFFFF'
black = '#000000'
red_black ='#DF0029'
red = '#E33539'
orange = '#EC870E'
green = '#00A06B'
blue = '#00BFFF'
violet = '#9B30FF'
pink = '#FF69B4'
yellow = '#FFFF00'
gray = '#707070'
brown = '#FAEBD7'
turtle_name = ['red', 'orange', 'green', 'blue', 'violet', 'pink']
turtle_name_n = [0, 1, 2, 3, 4, 5]
colors = [red, orange, green, blue, violet, pink]
turtle_speed = [5, 10, 15, 20, 25, 30]
all_turtles = []
# Màn hình
screen = Screen()
screen.setup(WIDTH, HEIGHT)
bgcolor(brown)
title('Đua rùa')

# Hàm vẽ hình chữ nhật
def rectangle_af(x, y, col):
    color(col)
    pensize(1)
    begin_fill()
    pendown()
    for i in range(2):
        fd(x)
        lt(90)
        fd(y)
        lt(90)
    end_fill()
    penup()
# 
# Vẽ đường đua
speed(0)
goto(-390, 293)
rt(90)
for i in range(6):
    rectangle_af(10, 840, white)
    fd(96)
rectangle_af(10, 840, white)
goto(0,-744)
lt(135)
for i in range(33):
    fd(32)
    rectangle_af(16, 1020, black)
goto(-390, 310)
rt(135)
rectangle_af(-570, 880, brown)
rectangle_af(17, 840, brown)
fd(17)
for i in range(6):
    fd(10)
    rectangle_af(86, 840, brown)
    fd(86)
fd(10)
rectangle_af(570, 840, brown)
goto(-390, 310)
rectangle_af(617, 20, yellow)
rectangle_af(627, -600, brown)
goto(420, 310)
rectangle_af(627, 600, brown)
rectangle_af(617, 20, yellow)

# Ô màu
goto(-443, 240)
for i in range(6):
    pendown()
    pencolor(colors[i])
    
    pensize(5)
    fillcolor(white)
    begin_fill()
    circle(25)
    end_fill()
    penup()
    fd(96)
goto(-428, 214)
for i in range(6):
    # pencolor(colors[i])
    pencolor(black)
    write('{}'.format(i+1), font=('FreeSans', 30))
    fd(96)
# Chữ
goto(-385, -296)
color(black)
write('X\nU\nẤ\nT\n \nP\nH\nÁ\nT\n \n||\n||\n||\n \nX\nU\nẤ\nT\n \nP\nH\nÁ\nT', font=('FreeSans', 15))
goto(425, -296)
write(' \n||\n||\n||\n \nĐ\n \nC\nH\n \n||\n||\n||\n \nĐ\n \nC\nH\n \n||\n||\n||\n ', font=('FreeSans', 15))
goto(429, -296)
write(' \n \n \n \n \n \nÍ\n \n \n \n \n \n \n \n \nÍ\n \n \n \n \n \n \n ', font=('FreeSans', 15))

penup()

# Di chuyển
def random_walk(turtles):
    speed(1)
    global run
    for turtle in turtles:
        # turtle.forward(choice(turtle_speed))    # chạy theo khoảng cách random 5 10 15 20 25 30
        turtle.forward(randint(1, 10))          # chạy theo khoảng cách random từ 1 tới 10
    # Thông báo rùa thắng cuộc. Và kết quả dự đoán
    # Thời gian chạy xong 
    end_time = time()
    speed(0)
    if turtles[0].xcor() >= 410:
        goto(-205, 109)
        color(red)
        write('Rùa đỏ chiến thắng!', font=('FreeSans', 35))
        time_run = round((end_time - start_time), 2)
        goto(-275, 13)
        write('Với thời gian là: {} Giây'.format(time_run), font=('FreeSans', 35))
        if guess == 'red' or guess == 'r' or guess == 'đỏ' or guess == 'do' or guess == 'd' or guess == '1':
            goto(-105, -83)
            write('Chúc mừng!', font=('FreeSans', 35))
            goto(-235, -179)
            write('Bạn đã đoán chính xác!', font=('FreeSans', 35))
        else:
            goto(-75, -83)
            write('Rất tiếc!', font=('FreeSans', 35))
            goto(-175, -179)
            write('Bạn đã đoán sai!', font=('FreeSans', 35))
        run = False
    elif turtles[1].xcor() >= 410:
        goto(-215, 109)
        color(orange)
        write('Rùa cam chiến thắng!', font=('FreeSans', 35))
        time_run = round((end_time - start_time), 2)
        goto(-275, 13)
        write('Với thời gian là: {} Giây'.format(time_run), font=('FreeSans', 35))
        if guess == 'orange' or guess == 'o' or guess == 'cam' or guess == 'c' or guess == '2':
            goto(-105, -83)
            write('Chúc mừng!', font=('FreeSans', 35))
            goto(-235, -179)
            write('Bạn đã đoán chính xác!', font=('FreeSans', 35))
        else:
            goto(-75, -83)
            write('Rất tiếc!', font=('FreeSans', 35))
            goto(-175, -179)
            write('Bạn đã đoán sai!', font=('FreeSans', 35))
        run = False
    elif turtles[2].xcor() >= 410:
        goto(-245, 109)
        color(green)
        write('Rùa xanh lá chiến thắng!', font=('FreeSans', 35))
        time_run = round((end_time - start_time), 2)
        goto(-275, 13)
        write('Với thời gian là: {} Giây'.format(time_run), font=('FreeSans', 35))
        if guess == 'green' or guess == 'g' or guess == 'xanh lá' or guess == 'xanh la' or guess == 'xl' or guess == '3':
            goto(-105, -83)
            write('Chúc mừng!', font=('FreeSans', 35))
            goto(-235, -179)
            write('Bạn đã đoán chính xác!', font=('FreeSans', 35))
        else:
            goto(-75, -83)
            write('Rất tiếc!', font=('FreeSans', 35))
            goto(-175, -179)
            write('Bạn đã đoán sai!', font=('FreeSans', 35))
        run = False
    elif turtles[3].xcor() >= 410:
        goto(-300, 109)
        color(blue)
        write('Rùa xanh dương chiến thắng!', font=('FreeSans', 35))
        time_run = round((end_time - start_time), 2)
        goto(-275, 13)
        write('Với thời gian là: {} Giây'.format(time_run), font=('FreeSans', 35))
        if guess == 'blue' or guess == 'b' or guess == 'xanh dương' or guess == 'xanh duong' or guess == 'xd' or guess == '4':
            goto(-105, -83)
            write('Chúc mừng!', font=('FreeSans', 35))
            goto(-235, -179)
            write('Bạn đã đoán chính xác!', font=('FreeSans', 35))
        else:
            goto(-75, -83)
            write('Rất tiếc!', font=('FreeSans', 35))
            goto(-175, -179)
            write('Bạn đã đoán sai!', font=('FreeSans', 35))
        run = False
    elif turtles[4].xcor() >= 410:
        goto(-215, 109)
        color(violet)
        write('Rùa tím chiến thắng!', font=('FreeSans', 35))
        time_run = round((end_time - start_time), 2)
        goto(-275, 13)
        write('Với thời gian là: {} Giây'.format(time_run), font=('FreeSans', 35))
        if guess == 'violet' or guess == 'v' or guess == 'tím' or guess == 'tim' or guess == 't' or guess == '5':
            goto(-105, -83)
            write('Chúc mừng!', font=('FreeSans', 35))
            goto(-235, -179)
            write('Bạn đã đoán chính xác!', font=('FreeSans', 35))
        else:
            goto(-75, -83)
            write('Rất tiếc!', font=('FreeSans', 35))
            goto(-175, -179)
            write('Bạn đã đoán sai!', font=('FreeSans', 35))
        run = False
    elif turtles[5].xcor() >= 410:
        goto(-225, 109)
        color(pink)
        write('Rùa hồng chiến thắng!', font=('FreeSans', 35))
        time_run = round((end_time - start_time), 2)
        goto(-275, 13)
        write('Với thời gian là: {} Giây'.format(time_run), font=('FreeSans', 35))
        if guess == 'pink' or guess == 'p' or guess == 'hồng' or guess == 'hong' or guess == 'h' or guess == '6':
            goto(-105, -83)
            write('Chúc mừng!', font=('FreeSans', 35))
            goto(-235, -179)
            write('Bạn đã đoán chính xác!', font=('FreeSans', 35))
        else:
            goto(-75, -83)
            write('Rất tiếc!', font=('FreeSans', 35))
            goto(-175, -179)
            write('Bạn đã đoán sai!', font=('FreeSans', 35))
        run = False

# Chơi game
while True:     
    run = True
    # Vị trí ban đầu của rùa
    x_position = (-420)
    y_position = [240, 144, 48, -48, -144, -240]
    # Create turtles
    for turtle in range(0, 6):
        turtles = Turtle(shape="turtle")
        turtles.penup()
        # Start
        turtles.goto(x=x_position, y=y_position[turtle])
        # Color
        turtles.color(colors[turtle])
        # Save
        all_turtles.append(turtles)
    # Nhập dự đoán của người dùng
    guess = screen.textinput(prompt='1-đỏ, 2-cam, 3-xanh lá, 4-xanh dương, 5-tím, 6-hồng', title='Dự đoán con rùa nào chiến thắng?')
    sleep(1)
    # Đếm ngược
    goto(-70, 13)
    color(red_black)
    write('Ready!', font=('FreeSans', 35))
    sleep(1)
    goto(-75, 89)
    rectangle_af(83, 200, brown)
    countdown= [3, 2, 1]
    for i in range(3):
        goto(-5, 13)
        color(red_black)
        write(countdown[i], font=('FreeSans', 35))
        sleep(1)
        goto(-75, 89)
        rectangle_af(83, 200, brown)
    goto(-25, 13)
    color(red_black)
    write('Go!', font=('FreeSans', 35))
    sleep(0.5)
    goto(-75, 89)
    rectangle_af(83, 200, brown)
    # Thời gian bắt đầu chạy
    start_time = time()
    while run:
        random_walk(all_turtles)
    sleep(3)
    if run == False:
        # Chơi lại
        play_again = screen.textinput(prompt='Bạn có muốn chơi lại không?', title='')
        if play_again == 'có' or play_again == 'co' or play_again == 'yes' or play_again == 'y' \
            or play_again == 'ok' or play_again == 'vâng' or play_again == 'vang'   \
            or play_again == 'dạ' or play_again == 'da' \
            or play_again == '1'or play_again == '11'or play_again == '111' or play_again == '':
            # Reset lại từ đầu
            all_turtles.clear()
            # Vẽ lại trường đua
            speed(0)
            goto(420, 293)
            for i in range(6):
                fd(10)
                rectangle_af(86, -789, brown)
                fd(86)
            fd(10)
            goto(420, 310)
            rectangle_af(627, 600, brown)
            rectangle_af(617, 20, yellow)
            # Chữ
            color(black)
            goto(425, -296)
            write(' \n||\n||\n||\n \nĐ\n \nC\nH\n \n||\n||\n||\n \nĐ\n \nC\nH\n \n||\n||\n||\n ', font=('FreeSans', 15))
            goto(429, -296)
            write(' \n \n \n \n \n \nÍ\n \n \n \n \n \n \n \n \nÍ\n \n \n \n \n \n \n ', font=('FreeSans', 15))
            continue
        else :
            break

screen.exitonclick()