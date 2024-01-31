def add_item(original, additonal) :
    '''Hàm thêm item vào list cho trước.
        Cú pháp: add_item(original, additonal)
            original: list ban đầu
            additonal: [ item cần thêm vào ] hoặc tên của list cần thêm vào
            Ví dụ: 
                fruits = ['Grape', 'Starfruit', 'Mangosteen', 'Durian']
                fruits_add = ['Peach', 'Longan', 'Berry']

                add_item(fruits, fruits_add)
                    hoặc
                add_item(fruits, ['Peach', 'Longan', 'Berry'])
                
                Kết quả: ['Grape', 'Starfruit', 'Mangosteen', 'Durian', 'Peach', 'Longan', 'Berry']'''
    for i in range(len(additonal)) :
        original.append(additonal[i])

# # test code
# fruits = ['Grape', 'Starfruit', 'Mangosteen', 'Durian']
# fruits_add = ['Peach', 'Longan', 'Berry']
# add_item(fruits, ['Peach', 'Longan', 'Berry'])
# add_item(fruits, fruits_add)
# add_item(fruits, ['Star apple', 2, 3, 'Watermelon'])
# print(fruits)
# print(add_item.__doc__)