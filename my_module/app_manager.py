# Tìm item theo ID, Tên và List
def find_item(list_item, item_find):
    result = -1
    if type(item_find) == int:
        for id in list_item:
            if id == item_find:
                result = item_find
                break
            else: 
                result = -1
        if result != -1:
            print('Product ID: {0}\n{0} = {1}'.format(item_find, list_item[id]))   
        elif result == -1:
            print('{} doesn\'t exists'.format(item_find))
    elif type(item_find) == str:
        for id in list_item:
            if list_item[id]['NAME'] == item_find:
                result = item_find
                break
            else: 
                result = -1
        if result != -1:
            print('Product NAME: {0}\n{1} = {2}'.format(item_find, id, list_item[id]))   
        elif result == -1:
            print('{} doesn\'t exists'.format(item_find))
    elif type(item_find) == list:
        for item in item_find:
            if type(item) == int:
                for id in list_item:
                    if id == item:
                        result = item
                        break
                    else: 
                        result = -1
                if result != -1:
                    print('Product ID: {0}\n{1} = {2}'.format(item, id, list_item[id]))      
                elif result == -1:
                    print('{} doesn\'t exists'.format(item))
            elif type(item) == str:
                for id in list_item:
                    if list_item[id]['NAME'] == item:
                        result = item
                        break
                    else: 
                        result = -1
                if result != -1:
                    print('Product NAME: {0}\n{1} = {2}'.format(item, id, list_item[id]))
                elif result == -1:
                    print('{} doesn\'t exists'.format(item))

# Thêm item
def add_item(original):
    while True:
        get_ID = []
        for id in original:
            get_ID.append(id)
            get_ID.sort()
            new_item_ID = get_ID[-1] + 1
        new_item_NAME = input('Enter new item\'s NAME: ')
        new_item_COST = int(input('Enter new item\'s COST: '))
        new_item_PRICE = int(input('Enter new item\'s PRICE: '))
        new_item_QUANTITY = int(input('Enter new item\'s QUANTITY: '))
        new_item_INPUT_DATE = input('Enter new item\'s INPUT_DATE: ')
        new_item_EXP = input('Enter new item\'s EXP: ')
        original.update({new_item_ID: {'NAME': new_item_NAME,   'COST': new_item_COST,  'PRICE': new_item_PRICE,     'QUANTITY':new_item_QUANTITY, 'INPUT_DATE': new_item_INPUT_DATE, 'EXP': new_item_EXP}})
        print('{0} : {1} has been added to the list'.format(new_item_ID, original[new_item_ID]))
        ask = input('Do you want to add more items?')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            continue
        else:
            break
    print('Your new products list:')
    for id in original:
        print(id, ':', original[id])

# Xóa item 
def remove_item(list_item, item_remove):
    result = -1
    if type(item_remove) == int:
        for id in list_item:
            if id == item_remove:
                result = item_remove
                break
            else: 
                result = -1
        if result != -1:
            print('Product ID: {0}\n{0} = {1}'.format(item_remove, list_item[id]))
            ask = input('Do you want to delete {}?\n\
                    Yes = 1\n\
                    No = 0\n\
                    '.format(item_remove))
            if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                list_item.pop(item_remove)
                print('{} has been deleted'.format(item_remove))
                print('Your new products list:')
                for id in list_item:
                    print(id, ':', list_item[id])
            else :
                print('Thank you!')
        elif result == -1:
            print('{} doesn\'t exists'.format(item_remove))
    elif type(item_remove) == str:
        for id in list_item:
            if list_item[id]['NAME'] == item_remove:
                result = item_remove
                break
            else: 
                result = -1
        if result != -1:
            print('Product NAME: {0}\n{1} = {2}'.format(item_remove, id, list_item[id]))
            ask = input('Do you want to delete {}?\n\
                    Yes = 1\n\
                    No = 0\n\
                    '.format(item_remove))
            if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                list_item.pop(id)
                print('{} has been deleted'.format(item_remove))
                print('Your new products list:')
                for id in list_item:
                    print(id, ':', list_item[id])
            else :
                print('Thank you!')
        elif result == -1:
            print('{} doesn\'t exists'.format(item_remove))
    elif type(item_remove) == list:
        for item in item_remove:
            if type(item) == int:
                for id in list_item:
                    if id == item:
                        result = item
                        break
                    else: 
                        result = -1
                if result != -1:
                    print('Product ID: {0}\n{1} = {2}'.format(item, id, list_item[id]))
                    ask = input('Do you want to delete {}?\n\
                        Yes = 1\n\
                        No = 0\n\
                        '.format(item))
                    if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                        if id == item:
                            list_item.pop(item)
                            print('{} has been deleted'.format(item))
                        print('Your new products list:')
                        for id in list_item:
                            print(id, ':', list_item[id])
                    else :
                        print('Thank you!')
                elif result == -1:
                    print('{} doesn\'t exists'.format(item))
            elif type(item) == str:
                for id in list_item:
                    if list_item[id]['NAME'] == item:
                        result = item
                        break
                    else: 
                        result = -1
                if result != -1:
                    print('Product NAME: {0}\n{1} = {2}'.format(item, id, list_item[id]))
                    ask = input('Do you want to delete {}?\n\
                        Yes = 1\n\
                        No = 0\n\
                        '.format(item))
                    if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                        if list_item[id]['NAME'] == item:
                            list_item.pop(id)
                            print('{} has been deleted'.format(item))
                        print('Your new products list:')
                        for id in list_item:
                            print(id, ':', list_item[id])
                    else :
                        print('Thank you!')
                elif result == -1:
                    print('{} doesn\'t exists'.format(item))

# Sửa item
def change_item(original, item_change):
    result = -1
    if type(item_change) == int:
        for id in original:
            if id == item_change:
                result = item_change
                break
            else: 
                result = -1
        if result != -1:
            print('Product ID: {0}\n{0} = {1}'.format(item_change, original[id]))
            ask = input('Do you want to change {}?\n\
                    Yes = 1\n\
                    No = 0\n\
                    '.format(item_change))
            if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                    get_ID = []
                    ask = input('Do you want to reuse the id or create a new one?\n\
                    Reuse the id = 1\n\
                    Create a new one = 0\n\
                    ')
                    if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
                        new_ID = id
                    else:
                        original.pop(item_change)
                        for id in original:
                            get_ID.append(id)
                            get_ID.sort()
                            new_ID = get_ID[-1] + 1
                    new_NAME = input('Enter new NAME of item: ')
                    new_COST = int(input('Enter new COST of item: '))
                    new_PRICE = int(input('Enter new PRICE of item: '))
                    new_QUANTITY = int(input('Enter new QUANTITY of item: '))
                    new_INPUT_DATE = input('Enter new INPUT_DATE of item: ')
                    new_EXP = input('Enter new EXP of item: ')
                    original.update({new_ID: {'NAME': new_NAME,   'COST': new_COST,  'PRICE': new_PRICE,     'QUANTITY':new_QUANTITY, 'INPUT_DATE': new_INPUT_DATE, 'EXP': new_EXP}})
                    print('{0} : {1} has been changed to the list'.format(new_ID, original[new_ID]))
            else :
                print('Thank you!')       
        elif result == -1:
            print('{} doesn\'t exists'.format(item_change))
    elif type(item_change) == str:
        for id in original:
            if original[id]['NAME'] == item_change:
                result = item_change
                break
            else: 
                result = -1
        if result != -1:
            print('Product NAME: {0}\n{1} = {2}'.format(item_change, id, original[id]))
            ask = input('Do you want to change {}?\n\
                    Yes = 1\n\
                    No = 0\n\
                    '.format(item_change))
            if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                    get_ID = []
                    ask = input('Do you want to reuse the id or create a new one?\n\
                    Reuse the id = 1\n\
                    Create a new one = 0\n\
                    ')
                    if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
                        new_ID = id
                    else:
                        original.pop(id)
                        for id in original:
                            get_ID.append(id)
                            get_ID.sort()
                            new_ID = get_ID[-1] + 1
                    new_NAME = input('Enter new NAME of item: ')
                    new_COST = int(input('Enter new COST of item: '))
                    new_PRICE = int(input('Enter new PRICE of item: '))
                    new_QUANTITY = int(input('Enter new QUANTITY of item: '))
                    new_INPUT_DATE = input('Enter new INPUT_DATE of item: ')
                    new_EXP = input('Enter new EXP of item: ')
                    original.update({new_ID: {'NAME': new_NAME,   'COST': new_COST,  'PRICE': new_PRICE,     'QUANTITY':new_QUANTITY, 'INPUT_DATE': new_INPUT_DATE, 'EXP': new_EXP}})
                    print('{0} : {1} has been changed to the list'.format(new_ID, original[new_ID]))
            else :
                print('Thank you!')   
        elif result == -1:
            print('{} doesn\'t exists'.format(item_change))
    elif type(item_change) == list:
        for item in item_change:
            if type(item) == int:
                for id in original:
                    if id == item:
                        result = item
                        break
                    else: 
                        result = -1
                if result != -1:
                    print('Product ID: {0}\n{1} = {2}'.format(item, id, original[id]))
                    ask = input('Do you want to change {}?\n\
                    Yes = 1\n\
                    No = 0\n\
                    '.format(item_change))
                    if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                        get_ID = []
                        ask = input('Do you want to reuse the id or create a new one?\n\
                    Reuse the id = 1\n\
                    Create a new one = 0\n\
                    ')
                        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
                            new_ID = id
                        else:
                            original.pop(item)
                            for id in original:
                                get_ID.append(id)
                                get_ID.sort()
                                new_ID = get_ID[-1] + 1
                        new_NAME = input('Enter new NAME of item: ')
                        new_COST = int(input('Enter new COST of item: '))
                        new_PRICE = int(input('Enter new PRICE of item: '))
                        new_QUANTITY = int(input('Enter new QUANTITY of item: '))
                        new_INPUT_DATE = input('Enter new INPUT_DATE of item: ')
                        new_EXP = input('Enter new EXP of item: ')
                        original.update({new_ID: {'NAME': new_NAME,   'COST': new_COST,  'PRICE': new_PRICE,     'QUANTITY':new_QUANTITY, 'INPUT_DATE': new_INPUT_DATE, 'EXP': new_EXP}})
                        print('{0} : {1} has been changed to the list'.format(new_ID, original[new_ID]))
                    else :
                        print('Thank you!')
                elif result == -1:
                    print('{} doesn\'t exists'.format(item))
            elif type(item) == str:
                for id in original:
                    if original[id]['NAME'] == item:
                        result = item
                        break
                    else: 
                        result = -1
                if result != -1:
                    print('Product NAME: {0}\n{1} = {2}'.format(item, id, original[id]))
                    ask = input('Do you want to change {}?\n\
                    Yes = 1\n\
                    No = 0\n\
                    '.format(item_change))
                    if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '' :
                        get_ID = []
                        ask = input('Do you want to reuse the id or create a new one?\n\
                    Reuse the id = 1\n\
                    Create a new one = 0\n\
                    ')
                        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
                            new_ID = id
                        else:
                            original.pop(id)
                            for id in original:
                                get_ID.append(id)
                                get_ID.sort()
                                new_ID = get_ID[-1] + 1
                        new_NAME = input('Enter new NAME of item: ')
                        new_COST = int(input('Enter new COST of item: '))
                        new_PRICE = int(input('Enter new PRICE of item: '))
                        new_QUANTITY = int(input('Enter new QUANTITY of item: '))
                        new_INPUT_DATE = input('Enter new INPUT_DATE of item: ')
                        new_EXP = input('Enter new EXP of item: ')
                        original.update({new_ID: {'NAME': new_NAME,   'COST': new_COST,  'PRICE': new_PRICE,     'QUANTITY':new_QUANTITY, 'INPUT_DATE': new_INPUT_DATE, 'EXP': new_EXP}})
                        print('{0} : {1} has been changed to the list'.format(new_ID, original[new_ID]))
                    else :
                        print('Thank you!')
                elif result == -1:
                    print('{} doesn\'t exists'.format(item))
    print('Your new products list:')
    for id in original:
        print(id, ':', original[id])

# Test code
# Database
products = { 
100001: {'NAME': 'product 1',   'COST': 15000,  'PRICE': 25000,     'QUANTITY':200, 'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2027'},
100002: {'NAME': 'product 2',   'COST': 25000,  'PRICE': 45000,     'QUANTITY':250, 'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2027'},
100003: {'NAME': 'product 3',   'COST': 18000,  'PRICE': 29000,     'QUANTITY':150, 'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2027'},
100004: {'NAME': 'product 4',   'COST': 45000,  'PRICE': 79000,     'QUANTITY':60,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2027'},
100005: {'NAME': 'product 5',   'COST': 99000,  'PRICE': 169000,    'QUANTITY':50,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2027'},
100006: {'NAME': 'product 6',   'COST': 150000, 'PRICE': 349000,    'QUANTITY':50,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
100007: {'NAME': 'product 7',   'COST': 98000,  'PRICE': 179000,    'QUANTITY':40,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
100008: {'NAME': 'product 8',   'COST': 77000,  'PRICE': 139000,    'QUANTITY':40,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
100009: {'NAME': 'product 9',   'COST': 65000,  'PRICE': 119000,    'QUANTITY':90,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
100010: {'NAME': 'product 10',  'COST': 97000,  'PRICE': 169000,    'QUANTITY':10,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
100011: {'NAME': 'product 11',  'COST': 49000,  'PRICE': 89000,     'QUANTITY':10,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
100012: {'NAME': 'product 12',  'COST': 85000,  'PRICE': 159000,    'QUANTITY':50,  'INPUT_DATE': '11/1/2024', 'EXP': '1/1/2025'},
}            


# # Tìm item -- Chạy ok
# find_item(products, 100008)
# find_item(products, 1000099)
# find_item(products, 'product 3')
# find_item(products, 'product 99')
# find_item(products, [100005, 100006])
# find_item(products, [100005, 1000066])
# find_item(products, ['product 7', 'product 11', 'product 16'])

# # Add item -- Chạy ok
# add_item(products)

# Xóa item -- Chạy ok
# remove_item(products, 100008)
# remove_item(products, 1000099)
# remove_item(products, 'product 3')
# remove_item(products, 'product 99')
# remove_item(products, [100005, 100006])
# remove_item(products, [100005, 1000066])
# remove_item(products, ['product 7', 'product 11', 100002])

# Change item -- Chạy ok
# change_item(products, 100008)
# change_item(products, 1000099)
# change_item(products, 'product 3')
# change_item(products, 'product 99')
# change_item(products, [100005, 100006])
# change_item(products, [100005, 1000066])
# change_item(products, ['product 7', 'product 11', 100002])

# Test print products
# for id in products:
#     print(id, ':', products[id])

while True:
    ask = input('Choose the option you want.\n\
                    Show list = 1\n\
                    Find item = 2\n\
                    Add item = 3\n\
                    Change item = 4\n\
                    Remove item = 5\n\
                    Exit = 0\n\
                    ')
    if ask == '1' or ask == 'Show list' or ask == 'show list' or ask == 'Show' or ask == 'show' or ask == 'S'  or ask == 's':
        for id in products:
            print(id, ':', products[id])
    elif ask == '2' or ask == 'Find item' or ask == 'find item' or ask == 'Find' or ask == 'find' or ask == 'F'  or ask == 'f':
        ask = input('Do you want to find Product ID or Product NAME?\n\
                    Product ID = 1\n\
                    Product NAME = 2\n\
                    ')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            product = int(input('Enter Product ID: '))
            find_item(products, product)
        elif ask == '2' or ask == 'No' or ask == 'no' or ask == 'N'  or ask == 'n':
            product = input('Enter Product NAME: ')
            find_item(products, product)
        else:
            print("Invalid input")
    elif ask == '3' or ask == 'Add item' or ask == 'add item' or ask == 'Add' or ask == 'add' or ask == 'A'  or ask == 'a':
        add_item(products)
    elif ask == '4' or ask == 'Change item' or ask == 'change item' or ask == 'Change' or ask == 'change' or ask == 'C'  or ask == 'c':
        ask = input('Do you want to find Product ID or Product NAME?\n\
                    Product ID = 1\n\
                    Product NAME = 2\n\
                    ')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            product = int(input('Enter Product ID: '))
            change_item(products, product)
        elif ask == '2' or ask == 'No' or ask == 'no' or ask == 'N'  or ask == 'n':
            product = input('Enter Product NAME: ')
            change_item(products, product)
        else:
            print("Invalid input")
    elif ask == '5' or ask == 'Remove item' or ask == 'remove item' or ask == 'Remove' or ask == 'remove' or ask == 'R'  or ask == 'r':
        ask = input('Do you want to find Product ID or Product NAME?\n\
                    Product ID = 1\n\
                    Product NAME = 2\n\
                    ')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            product = int(input('Enter Product ID: '))
            remove_item(products, product)
        elif ask == '2' or ask == 'No' or ask == 'no' or ask == 'N'  or ask == 'n':
            product = input('Enter Product NAME: ')
            remove_item(products, product)
        else:
            print("Invalid input")
    else:
        print('Thank you!\nSee you again!')
        break
