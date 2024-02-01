def get_min_number(numbers_list) :
    min = numbers_list[0]
    for i in range(len(numbers_list)) :
        if min > numbers_list[i] :
            min = numbers_list[i]
        if i == len(numbers_list) - 1 :     
            print(min)
            

# # test code
# get_min_number([12,23,34,32,12,43,534,234,23,1,99])