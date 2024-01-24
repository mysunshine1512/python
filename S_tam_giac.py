import math
a = float(input("Nhap chieu dai canh a: "))
b = float(input("Nhap chieu dai canh b: "))
c = float(input("Nhap chieu dai canh c: "))
s = (a + b + c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print ("Dien tich hinh tam giac la: ", area)