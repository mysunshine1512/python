shape_input = int(input("Nhập số cạnh của hình đa giác đều mà bạn muốn vẽ ( từ 3 đến 18 ), nếu muốn vẽ hình tròn thì nhập 360 "))
if shape_input == 360 or 3<= shape_input <= 18  :
    size_input = int(input("Nhập kích thước của hình bạn muốn vẽ: "))
    if 0 < size_input <= 360 :
        pensize_input = int(input("Nhập kích thước của nét bút: "))
        if 0 < pensize_input <=30 :
            color_input = input("Nhập màu sắc bạn thích bằng tiếng anh (ví du: red, yellow, purple, ...): ")
            if color_input == "aqua" or color_input == "black" or color_input == "blue" or color_input == "green"  \
            or color_input == "red" or color_input == "yellow" or color_input == "orange" or color_input == "pink"  \
            or color_input == "brown" or color_input == "purple"  or color_input == "gray" :
                from turtle import *
                speed(1000)
                hideturtle()
                title("Đây là hình vẽ của bạn! Chúc bạn một ngày tốt lành!")
                pensize(pensize_input)
                pencolor(color_input)
                penup()
                goto(0, - size_input)
                pendown()
                circle(size_input, steps=(shape_input))
                done()
            elif color_input == "" :
                from turtle import *
                pensize(pensize_input)
                bgcolor("white")
                speed(100)
                hideturtle()
                n = int(0)
                for i in range(48) :
                    n = n + 1
                    if n == 1 or n == 13 or n == 25 or n == 37:
                        color("#DF0029")
                    elif n == 2 or n == 14  or n == 26 or n == 38:
                        color("#E33539")
                    elif n == 3 or n == 15  or n == 27 or n == 39:
                        color("#EC870E")
                    elif n == 4 or n == 16  or n == 28 or n == 40:
                        color("#F1AF00")
                    elif n == 5 or n == 17  or n == 29 or n == 41:
                        color("#F9F400")
                    elif n == 6 or n == 18  or n == 30 or n == 42:
                        color("#5BBD2B")
                    elif n == 7 or n == 19  or n == 31 or n == 43:
                        color("#00A06B")
                    elif n == 8 or n == 20 or n == 32 or n == 44:
                        color("#00A6AD")
                    elif n == 9 or n == 21  or n == 33 or n == 45:
                        color("#205AA7")
                    elif n == 10 or n == 22  or n == 34 or n == 46:
                        color("#3A2885")
                    elif n == 11 or n == 23  or n == 35 or n == 47:
                        color("#5D0C7B")
                    elif n == 12 or n == 24  or n == 36 or n == 48:
                        color("#A2007C") 
                    else :
                        color("white") 
                    pencolor = color
                    pensize(pensize_input)
                    penup()
                    goto(0, - size_input + pensize_input * n)
                    pendown()
                    fillcolor = color
                    begin_fill()
                    circle(size_input - pensize_input * n , steps=(shape_input))
                    end_fill()
                    if - size_input + pensize_input * n > - 10 : 
                        done()
                done()
            else :
                print("Chúng tôi không có màu bạn chọn. Xin vui lòng nhập lại!")
        elif pensize_input <= 0 :
            print("Kích thước nét bút phải lớn hơn 0. Xin vui lòng nhập lại!")
        else :
            print("Kích thước nét bút tối đa là 30. Xin vui lòng nhập lại!")       
    elif 360 >= size_input > 0 :
        print("ngôi sao")
    elif size_input < 0 :
        print("Kích thước phải lớn hơn 0. Xin vui lòng nhập lại!")           
    else :       
        print("Kích thước tối đa là 360. Xin vui lòng nhập lại!")
else :
    print("Không thể vẽ hình của bạn. Xin vui lòng nhập lại!")