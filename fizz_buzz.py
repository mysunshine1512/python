start = int(input('Nhập số bắt đầu: '))
end = int(input('Nhập số kết thúc: '))
if start > end :
    print('Số kết thúc phải lớn hơn số bắt đầu!')
else :
    for i in range (start, end + 1) :
        if start % 3 == 0 and start % 5 == 0 :
            print('FizzBuzz')
        elif start % 3 == 0 :
            print('Fizz')
        elif start % 5 == 0 :
            print('Buzz')
        else :
            print(start)
        start += 1
        if start > end :
            break
        
