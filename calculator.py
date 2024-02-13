from tkinter import*
from math import*

# Color
orange = '#F5A045'
darkgray = '#696969'
gray = '#CFCFCF'
lighgray = '#F5F5F5'
black = '#000000'
white = '#FFFFFF'

# Màn hình ứng dụng
cal = Tk()
cal.geometry('500x700')
cal.title('Calculator Machine')
cal.configure(background= darkgray)

# Khai báo ban đầu
equation = ''
expression = StringVar()

# Viết chữ vào màn hình
def write(char):
    global equation
    equation += str(char)
    expression.set(equation)

# Nút xóa toàn bộ expression
def button_all_clear():
    global equation
    equation = ''
    expression.set('')

# Nút xóa 1 ký tự trong expression
def button_backspace():
    global equation
    text = equation[:-1]
    equation = text
    expression.set(text)

# Nút đổi dấu số
def sign_change():
    global equation
    if equation[0] == '-':
        temp = equation[1:]
    else:
        temp = '-' + equation
    equation = temp
    expression.set(temp)

# Nút %
def button_percent():
    global equation
    temp = str(eval(equation+'/100'))
    equation = temp
    expression.set(temp)

# Nút =
def button_equal():
    global equation
    temp_output = str(eval(equation))
    equation = temp_output
    expression.set(temp_output)


# expression
display = Entry(cal, font=('arial rounded mt', 32), textvariable=expression, background= white, justify= 'right', width=18).place(x=30, y=50)
# Button
# 1
button_div = Button(cal, text='div', font=('arial rounded mt', 25), command=lambda: write('//'), relief=RAISED, width=3, height=1).place(x=30, y=150)
button_mod = Button(cal, text='mod', font=('arial rounded mt', 25), command=lambda: write('%'), relief=RAISED, width=3, height=1).place(x=119, y=150)
button_exp = Button(cal, text='EXP', font=('arial rounded mt', 25), command=lambda: write('*10**'), relief=RAISED, width=3, height=1).place(x=213, y=150)
button_square_root = Button(cal, text='\N{square root}', command=lambda: write('**(1/'), font=('arial rounded mt', 25), relief=RAISED, width=3, height=1).place(x=307, y=150)
button_circumflex_accent = Button(cal, text='\N{circumflex accent}', font=('arial rounded mt', 25), command=lambda: write('**'), relief=RAISED, width=3, height=1).place(x=401, y=150)
# 2
button_open_parenthesis = Button(cal, text='\N{left parenthesis}', font=('arial rounded mt', 25), command=lambda: write('('), relief=RAISED, width=3, height=1).place(x=30, y=239)
button_close_parenthesis = Button(cal, text='\N{right parenthesis}', font=('arial rounded mt', 25), command=lambda: write(')'), relief=RAISED, width=3, height=1).place(x=119, y=239)
button_plus_and_minus = Button(cal, text='\u00B1', font=('arial rounded mt', 25), command=sign_change, relief=RAISED, width=3, height=1).place(x=213, y=239)
button_percent_btn = Button(cal, text='\N{percent sign}', font=('arial rounded mt', 25), command=button_percent, relief=RAISED, width=3, height=1).place(x=307, y=239)
button_pi = Button(cal, text='𝛑', font=('arial rounded mt', 25), command=lambda: write(pi), relief=RAISED, width=3, height=1).place(x=401, y=239)
# 3
button_7 = Button(cal, text='7', font=('arial rounded mt', 25), command=lambda: write('7'), relief=RAISED, width=3, height=1).place(x=30, y=328)
button_8 = Button(cal, text='8', font=('arial rounded mt', 25), command=lambda: write('8'), relief=RAISED, width=3, height=1).place(x=119, y=328)
button_9 = Button(cal, text='9', font=('arial rounded mt', 25), command=lambda: write('9'), relief=RAISED, width=3, height=1).place(x=213, y=328)
button_backspace_btn = Button(cal, text='\N{LEFTWARDS BLACK ARROW}', font=('arial rounded mt', 25), background=orange, command=button_backspace, relief=RAISED, width=3, height=1).place(x=307, y=328)
button_all_clear_btn = Button(cal, text='AC', font=('arial rounded mt', 25), background=orange, command=button_all_clear, relief=RAISED, width=3, height=1).place(x=401, y=328)
# 4
button_4 = Button(cal, text='4', font=('arial rounded mt', 25), command=lambda: write('4'), relief=RAISED, width=3, height=1).place(x=30, y=417)  #307
button_5 = Button(cal, text='5', font=('arial rounded mt', 25), command=lambda: write('5'), relief=RAISED, width=3, height=1).place(x=119, y=417)  # 401
button_6 = Button(cal, text='6', font=('arial rounded mt', 25), command=lambda: write('6'), relief=RAISED, width=3, height=1).place(x=213, y=417)
button_plus = Button(cal, text='\N{plus sign}', font=('arial rounded mt', 25), command=lambda: write('+'), relief=RAISED, width=3, height=1).place(x=307, y=417)
button_minus = Button(cal, text='\N{minus sign}', font=('arial rounded mt', 25), command=lambda: write('-'), relief=RAISED, width=3, height=1).place(x=401, y=417)
# 5
button_1 = Button(cal, text='1', font=('arial rounded mt', 25), command=lambda: write('1'), relief=RAISED, width=3, height=1).place(x=30, y=506)
button_2 = Button(cal, text='2', font=('arial rounded mt', 25), command=lambda: write('2'), relief=RAISED, width=3, height=1).place(x=119, y=506)
button_3 = Button(cal, text='3', font=('arial rounded mt', 25), command=lambda: write('3'), relief=RAISED, width=3, height=1).place(x=213, y=506)
button_multiply = Button(cal, text='\N{multiplication sign}', font=('arial rounded mt', 25), command=lambda: write('*'), relief=RAISED, width=3, height=1).place(x=307, y=506)
button_divide = Button(cal, text='\N{division sign}', font=('arial rounded mt', 25), command=lambda: write('/'), relief=RAISED, width=3, height=1).place(x=401, y=506)
# 6
button_0 = Button(cal, text='0', font=('arial rounded mt', 25), command=lambda: write('0'), relief=RAISED, width=3, height=1).place(x=30, y=595)
button_00 = Button(cal, text='00', font=('arial rounded mt', 25), command=lambda: write('00'), relief=RAISED, width=3, height=1).place(x=119, y=595)
button_full_stop = Button(cal, text='\N{full stop}', font=('arial rounded mt', 25), command=lambda: write('.'), relief=RAISED, width=3, height=1).place(x=213, y=595)
button_equal_btn = Button(cal, text='\N{equals sign}', font=('arial rounded mt', 25), command=button_equal, relief=RAISED, width=8, height=1).place(x=307, y=595)

cal.mainloop()