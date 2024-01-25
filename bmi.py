chieu_cao = float(input("Nhập số đo chiều cao (mét): "))
can_nang = float(input("Nhập số đo cân nặng (kg): "))
BMI = round(can_nang / (chieu_cao ** 2), 2)
print("BMI của bạn là: {}".format(BMI))
if BMI < 16 :
    print("Gầy cấp độ III")
elif BMI < 17 :
    print("Gầy cấp độ II")
elif BMI < 18.5 :
    print("Gầy cấp độ I")
elif BMI < 25 :
    print("Bình thường")
elif BMI < 30 :
    print("Thừa cân")
elif BMI < 35 :
    print("Béo phì cấp độ I")
elif BMI < 40 :
    print("Béo phì cấp độ II")
else :
    print("Béo phì cấp độ III")