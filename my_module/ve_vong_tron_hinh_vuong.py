from turtle import *
def square(size_square, size_circle, step) :
    '''Hàm vẽ vòng tròn bằng hình vuông.
        Cú pháp là: square(size_square, size_circle, step)
            size_square: kích thước hình vuông.
            size_circle: khoảng cách giữa mỗi hình vuông.
            step: số hình vuông bao quanh.
            Ví dụ: 
                square(20, 25, 36)
                done()'''
    for i in range(step) :
        pendown()
        for i in range(4) :
            fd(size_square)
            lt(90)
        penup()
        angle = 360 / step
        lt(angle)
        fd(size_circle)