usd = float(input( "Nhập số tiền USD: "))
rate = float(input( "Nhập tỉ giá: "))
vnd = usd * rate
print( "Giá trị VND theo tỉ giá {rate} là {vnd}".format(rate = rate, vnd = vnd))