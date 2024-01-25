so_tien = int(input("Nhập số tiền đã chi tiêu: "))
if so_tien < 75 :
    print("Số tiền thanh toán là: {}$".format(so_tien))
elif so_tien < 100 :
    print("Số tiền thanh toán là: {}$".format(so_tien - 15))
elif so_tien < 150 :
    print("Số tiền thanh toán là: {}$".format(so_tien - 25))
else :
    print("Số tiền thanh toán là: {}$".format(so_tien - 50))