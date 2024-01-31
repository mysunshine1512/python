# input a, b, c
# xét đk: a, b, c lớn nhất
A = float(input("Nhập A: "))
B = float(input("Nhập B: "))
C = float(input("Nhập C: "))
MAX = A
if A < B :
    MAX = B
if B < C :
    MAX = C
print("MAX = {}".format(MAX))