from turtle import *
from time import *
from math import *

gold = '#FFC717'
lighgold = '#FFFFF0'
white = '#FFFFFF'
black = '#000000'
silver = '#C0C0C0'
gray = '#4F4F4F'
lightgray = '#E8E8E8'
darkgray = '#B4B4B8'

class Clock:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def run(self):
        # Vẽ mặt đồng hồ
        # Khung và nền
        hideturtle()
        speed(0)
        penup()
        goto(self.x, self.y - self.r)
        pensize(1)
        pendown()
        color(gold)
        begin_fill()
        circle(self.r)
        end_fill()
        penup()
        goto(self.x, self.y - self.r * 0.88)
        pendown()
        color(lighgold)
        begin_fill()
        circle(self.r * 0.88)
        end_fill()
        penup()
        goto(self.x, self.y - self.r * 0.03)
        pensize(1)
        pendown()
        color(gold)
        begin_fill()
        circle(self.r * 0.03)
        end_fill()
        penup()

        # Vạch giờ
        goto(self.x, self.y)
        lt(90)
        for i in range(12):
            color(gold)
            fd(self.r * 0.88 - (self.r * 0.88 * 0.25))
            pendown()
            begin_fill()
            for i in range(2):
                fd(self.r * 0.88  * 0.25)
                rt(90)
                fd(self.r / 120)
                rt(90)
            for i in range(2):
                fd(self.r * 0.88  * 0.25)
                lt(90)
                fd(self.r / 120)
                lt(90)
            end_fill()
            penup()
            goto(self.x, self.y)
            rt(6)
            for i in range(4):
                color(darkgray)
                fd(self.r * 0.88 - (self.r * 0.88 * 0.1))
                pendown()
                begin_fill()
                for i in range(2):
                    fd(self.r * 0.88  * 0.1)
                    rt(90)
                    fd(self.r / 360)
                    rt(90)
                for i in range(2):
                    fd(self.r * 0.88  * 0.1)
                    lt(90)
                    fd(self.r / 360)
                    lt(90)
                end_fill()
                penup()
                goto(self.x, self.y)
                rt(6)
        rt(90)
        pensize(ceil(self.r / 120))
        goto(self.x, self.y - self.r * 0.88)
        pendown()
        color(lightgray)
        circle(self.r * 0.88)
        penup()

        # Ngày
        lt(90)
        color(white)
        goto(self.x, self.y - self.r * 0.65)
        pendown()
        begin_fill()
        for i in range(2):
            fd(self.r * 0.14)
            rt(90)
            fd(self.r * 0.075)
            rt(90)
        for i in range(2):
            fd(self.r * 0.14)
            lt(90)
            fd(self.r * 0.075)
            lt(90)
        end_fill()
        penup()
        lt(90)
        bk(self.r * 0.075)
        color(lightgray)
        pendown()
        for i in range(2):
            fd(self.r * 0.15)
            rt(90)
            fd(self.r * 0.14)
            rt(90)
        rt(90)
        penup()
        color(black)
        goto(self.x, self.y - self.r * 0.6525)
        write('30', align='center', font=('arial', ceil(self.r * 0.09), 'normal')) # Nhập DAY sau
        rt(90)
        
        # Chữ
        color(silver)
        goto(self.x, self.y + self.r * 0.45)
        write('TISSOT', align='center', font=('ClassicGrotesqueW04-ExBd', ceil(self.r * 0.05), 'normal'))
        goto(self.x, self.y + self.r * 0.4)
        write('1853', align='center', font=('Century Gothic', ceil(self.r * 0.04), 'normal'))
        goto(self.x, self.y - self.r * 0.2)
        write('PR100', align='center', font=('Century Gothic', ceil(self.r * 0.03), 'normal'))
        goto(self.x, self.y - self.r * 0.25)
        write('CHRONOMETER', align='center', font=('Century Gothic', ceil(self.r * 0.03), 'normal'))
        goto(self.x, self.y - self.r * 0.3)
        write('OFFICIALLY CERTIFIED', align='center', font=('Century Gothic', ceil(self.r * 0.03), 'normal'))
        goto(self.x, self.y - self.r * 0.35)
        write('SWISS MADE', align='center', font=('Century Gothic', ceil(self.r * 0.03), 'normal'))

        # Kim giây
        second_shape = (
                        (self.x + self.r / 360, self.y + self.r * (285/360)), \
                        (self.x + self.r / 360, self.y + self.r / 120), \
                        (self.x + self.r / 120, self.y + self.r / 120), \
                        (self.x + self.r / 120, self.y - self.r / 5), \
                        (self.x + self.r / 30, self.y - self.r / 5), \
                        (self.x + self.r / 30, self.y - self.r / 4.5), \
                        (self.x - self.r / 30, self.y - self.r / 4.5), \
                        (self.x - self.r / 30, self.y - self.r / 5), \
                        (self.x - self.r / 120, self.y - self.r / 5), \
                        (self.x - self.r / 120, self.y + self.r / 120), \
                        (self.x - self.r / 360, self.y + self.r / 120), \
                        (self.x - self.r / 360, self.y + self.r * (285/360)), \
                        )
        register_shape('second hand', second_shape)
        
        # Kim phút
        minute_shape = (
                        (self.x + self.r / 120, self.y + self.r * (275/360)), \
                        (self.x + self.r / 60, self.y + self.r * (272/360)), \
                        (self.x + self.r / 60, self.y - self.r / 14.4), \
                        (self.x + self.r / 120, self.y - self.r * (28/360)), \
                        (self.x - self.r / 120, self.y - self.r * (28/360)), \
                        (self.x - self.r / 60, self.y - self.r / 14.4), \
                        (self.x - self.r / 60, self.y + self.r * (272/360)), \
                        (self.x - self.r / 120, self.y + self.r * (275/360)), \
                        )
        register_shape('minute hand', minute_shape)
        
        # Kim giờ
        hour_shape = (
                        (self.x + self.r / 120, self.y + self.r * (185/360)), \
                        (self.x + self.r / 60, self.y + self.r * (182/360)), \
                        (self.x + self.r / 60, self.y - self.r / 14.4), \
                        (self.x + self.r / 120, self.y - self.r * (28/360)), \
                        (self.x - self.r / 120, self.y - self.r * (28/360)), \
                        (self.x - self.r / 60, self.y - self.r / 14.4), \
                        (self.x - self.r / 60, self.y + self.r * (182/360)), \
                        (self.x - self.r / 120, self.y + self.r * (185/360)), \
                        )
        register_shape('hour hand', hour_shape)
        
        

        hour_hand = Turtle()
        hour_hand.shape('hour hand')
        hour_hand.color(gold)
        hour_hand.lt(180)
        
        minute_hand = Turtle()
        minute_hand.shape('minute hand')
        minute_hand.color(gold)
        minute_hand.lt(90)

        second_hand = Turtle()
        second_hand.shape('second hand')
        second_hand.color(gold)
        second_hand.lt(90)
        while True:
            second_hand.rt(1) 
            minute_hand.rt(0.01)
            hour_hand.rt(0.00002314814)
        done()

c = Clock(360, 0, 0)
c.run()



# all_turtles =[]
# all_turtles.append(turtles)
# turtles = Turtle()
# turtles.fd(20)

# pendown()
# rt(90)
# fd(20)

done()

