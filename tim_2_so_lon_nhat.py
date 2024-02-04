numbers_list = [2, 3, 45, 90, 86, 998, 342, 12, 60, 645, 67, 976, 202, 40, 56, 77]

# cách 1
numbers_list.sort()
if len(numbers_list) == 0:
    print('List rỗng')
elif len(numbers_list) ==1:
    print('Số lớn nhất của list là: {}'.format(numbers_list[-1]))
else:
    print('Hai số lớn nhất của list là: {} và {}'.format(numbers_list[-1], numbers_list[-2]))

# cách 2
numbers_list.sort(reverse=True)
if len(numbers_list) == 0:
    print('List rỗng')
elif len(numbers_list) ==1:
    print('Số lớn nhất của list là: {}'.format(numbers_list[0]))
else:
    print('Hai số lớn nhất của list là: {} và {}'.format(numbers_list[0], numbers_list[1]))
