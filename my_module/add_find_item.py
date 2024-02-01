# thêm item in code
def add_item_(original, additonal) :
    for i in range(len(additonal)) :
        original.append(additonal[i])

# tìm item in code
def find_item_(list, find_name) :
    result = -1
    for i in range(len(list)) :
        if list[i]['NAME'] == find_name :
            result = i
    return result

# thêm item
def add_item(original) :
    new_item_name = input('Enter new item\'s name: ')
    new_item_cost = int(input('Enter new item\'s cost: '))
    new_item_date = input('Enter new item\'s date: ')
    additonal = {'NAME': new_item_name, 'COST': new_item_cost, 'DATE': new_item_date}
    add_item_(original, [additonal])
    print('{} has been added to the list'.format(additonal))
    print('Your new expenses list:', original)

# xóa item 
def remove_item(list, item_remove):
    if find_item_(list, item_remove) > -1:
        print('Your expenses list:', list)
        ask = input('Do you want to delete {}?\n\
                        Yes = 1\n\
                        No = 0\n\
                        '.format(item_remove))
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
            del list[find_item_(list, item_remove)]
            print('{} has been deleted'.format(item_remove))
        else :
            print('Thank you!')
    else:
        print('{} not in list'.format(item_remove))
        print('Your expenses list:', list)

# hiển thị list
def show_list(list) :
    ask = input('Your expenses list: {}\n\
        What do you want to do? \n\
            1. Add\n\
            2. Remove\n\
            '.format(list))
    if ask == '1' or ask == 'Add' or ask == 'add' or ask == 'ad' or ask == 'a' :
        # new_item = input('Enter new item: ')
        new_item_name = input('Enter new item\'s name: ')
        new_item_cost = int(input('Enter new item\'s cost: '))
        new_item_date = input('Enter new item\'s date: ')
        new_item = {'NAME': new_item_name, 'COST': new_item_cost, 'DATE': new_item_date}
        add_item_(list, [new_item])
        print('{} has been added to the list'.format(new_item))
        print('Your new expenses list:', list)
    elif ask == '2' or ask == 'Remove' or ask == 'remove' or ask == 'rm' or ask == 're' or ask == 'r' :
        ask = input('Enter expenses you want to delete:\n')
        for i in range(len(list)) :
            if list[i]['NAME'] == ask :
                remove_item(list, ask)
                break
    else:
        print("Invalid input")

# tìm và hiển thị item
def find_item(list, item) :
    find_item_(list, item)
    ask = input('Your expenses : {}\n\
    What do you want to do? \n\
            1. Change\n\
            2. Remove\n\
            '.format(list[find_item_(list, item)]))
    if ask == '1' or ask == 'Change' or ask == 'change' or ask == 'ch' or ask == 'c' :
        new_item_name = input('Enter new name of item: ')
        new_item_cost = int(input('Enter new cost of item: '))
        new_item_date = input('Enter new date of item: ')
        list[find_item_(list, item)].update({'NAME': new_item_name, 'COST': new_item_cost, 'DATE': new_item_date})
        print('Expenses has been modified')
        print('Your new expenses :', list[find_item_(list, new_item_name)])
    elif ask == '2' or ask == 'Remove' or ask == 'remove' or ask == 'rm' or ask == 're' or ask == 'r' :
        remove_item(list, item)
    else:
            print("Invalid input")

# test code   
# test1 = {'NAME': 'test 1', 'COST': 15000, 'DATE': '11/01/2024'}
# test2 = {'NAME': 'test 2', 'COST': 32000, 'DATE': '15/01/2024'}
# test3 = {'NAME': 'test 3', 'COST': 21000, 'DATE': '18/01/2024'}
# test4 = {'NAME': 'test 4', 'COST': 39000, 'DATE': '24/01/2024'}

# chi_tieu = [test1, test2, test3, test4]

# test5 = {'NAME': 'test 5', 'COST': 17000, 'DATE': '31/01/2024'}
# test6 = {'NAME': 'test 6', 'COST': 30000, 'DATE': '01/02/2024'}

# add_item(chi_tieu)
# remove_item(chi_tieu, 'test 5')
# add_item_(chi_tieu, [test5, test6])
# print(find_item_(chi_tieu, 'test 3'))
# remove_item(chi_tieu, 'test 4')
# show_list(chi_tieu)
# ask = (input('Enter expenses you want to delete:\n'))
# ask = {}
# print(type(ask))
# print(test1['NAME'])
# print(chi_tieu[2]['NAME'])
# show_item(chi_tieu, 'test 3')
# print(chi_tieu)
# find_item(chi_tieu, 'test 3')


# print(chi_tieu)




