# input a, b, c
# xét đk: a, b, c lớn nhất
A = float(input("Nhập A: "))
B = float(input("Nhập B: "))
C = float(input("Nhập C: "))
if A == B and A == C :
    print("3 số A B C bằng nhau, đều bằng {}".format(A))
# từ đây
elif A == B :
    if A > C :
        print("Số lớn nhất là A và B, đều bằng {}".format(A))
    else :
        print("Số lớn nhất là C, bằng {}".format(C))
elif A == C :
    if A > B :
        print("Số lớn nhất là A và C, đều bằng {}".format(A))
    else :
        print("Số lớn nhất là B, bằng {}".format(B))
elif B == C :
    if B > A :
        print("Số lớn nhất là B và C, đều bằng {}".format(B))
    else :
        print("Số lớn nhất là A, bằng {}".format(A))
# đến đây : có thể không cần nếu chỉ đơn giản là tìm số lớn nhất. Còn nếu muốn so sánh 3 số A B C thì bỏ vào
elif A > B :
    if A > C :
        print("Số lớn nhất là A, bằng {}".format(A))
    else :
        print("Số lớn nhất là C, bằng {}".format(C))
elif A < B :
    if B > C :
        print("Số lớn nhất là B, bằng {}".format(B))
    else :
        print("Số lớn nhất là C, bằng {}".format(C))
else :
    print("Số lớn nhất là C, bằng {}".format(C))