# nhập từ bàn phím
def count_chars_keyboard() :
    input_str = input('Enter your string: ')
    for i in range(len(input_str)) :
        if i == (len(input_str)) -1 :
            print('Length of string =',i + 1)

# nhập trực tiếp
def count_chars(input_str) :
    for i in range(len(input_str)) :
        if i == (len(input_str)) -1 :
            print('Length of string =',i + 1)

# # test code
# count_chars_keyboard()
# count_chars('ký tự bất kỳ')
