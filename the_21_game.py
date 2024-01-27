from random import *
while True :
    current_number = 0
    coin = randint(0, 1)
    while coin == 0 or coin == 1 :
        if coin == 0 :
            print('Lượt chơi của bạn')
            print('Số hiện tại là: {}'.format(current_number))
            player_choice = int(input('Nhập số 1 hoặc 2 hoặc 3. Số mà bạn nhập là: '))
            if player_choice == 1 or player_choice == 2 or player_choice == 3 :
                current_number += player_choice
                coin =1
                if current_number >= 21 :
                    print('Số hiện tại là: {}'.format(current_number))  
                    print('Bạn đã thua! Chúc bạn may mắn lần sau!')
                    break
            else :
                print(' Xin vui lòng thử lại!')
                coin = 0
        if coin == 1 :         
            print('Lượt chơi của Robot Siêu Thông Minh')
            print('Số hiện tại là: {}'.format(current_number))
            number_random = int(randint(1,3))
            computer_choice = number_random
            print('Số mà Robot Siêu Thông Minh đã nhập là: {}'.format(computer_choice))
            current_number += computer_choice
            coin = 0
            if current_number >= 21 :
                print('Số hiện tại là: {}'.format(current_number))
                print('Chúc mừng! Bạn đã chiến thắng!')
                break
    if current_number >= 21 :
        play_again = input('Bạn có muốn chơi lại không? ')
        if play_again == 'có' or play_again == 'co' or play_again == 'yes' or play_again == 'y' \
        or play_again == 'ok' or play_again == 'vâng' or play_again == 'vang'   \
        or play_again == 'dạ' or play_again == 'da' :
            continue
        else :
            break
