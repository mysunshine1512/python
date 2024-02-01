def add(num1, num2) :
    return num1 + num2
  
def subtract(num1, num2) :
    return num1 - num2
  
def multiply(num1, num2) :
    return num1 * num2

def divide(num1, num2) :
    return num1 / num2

def exponential(num1, num2) :
    return num1 ** num2

number_1 = float(input("Nhập số thứ nhất: "))
number_2 = float(input("Nhập số thứ hai: "))
option = input("Chọn phép toán: +, -, *, /, ^ ")

if option == '+':
    print(number_1, "+", number_2, "=", add(number_1, number_2))
  
elif option == '-':
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
  
elif option == '*':
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
  
elif option == '/':
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

elif option == '^':
    print(number_1, "^", number_2, "=", exponential(number_1, number_2))
    
else:
    print("Phép toán không hợp lệ.")
