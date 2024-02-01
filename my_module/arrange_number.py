def arrange() :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    num1 = a
    num2 = b
    num3 = c
    if a > c :
        if c >= b :
            num1 = b
            num2 = c
            num3 = a
        elif b > c :
            num1 = c
            num2 = b
            num3 = a
    elif b > c :
        if c >= a :
            num1 = a
            num2 = c
            num3 = b
    elif a > b :
        if b >= c :
            num1 = c
            num2 = b
            num3 = a
        elif b < c :
            num1 = b
            num2 = a
            num3 = c

    print("Original numbers: ", a, b, c)
    print("Sorted numbers: ", num1, num2, num3)

# test code
arrange()