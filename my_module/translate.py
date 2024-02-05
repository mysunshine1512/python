def translate(dictionary, word_input):
    translated_word = []
    for word in dictionary:
        if word == word_input:
            translated_word.append(dictionary[word])
    if len(translated_word) > 0:
        print(word_input, ':', translated_word[0])
    else:
        print(word_input, 'is not in the dictionary')

# Test code
# Từ điển
english = {
            'không'  : 'zero',
            'một'    : 'one',
            'hai'    : 'two',
            'ba'     : 'three',
            'bốn'    : 'four',
            'năm'    : 'five',
            'sáu'    : 'six',
            'bảy'    : 'seven',
            'tám'    : 'eight',
            'chín'   : 'nine',
            'mười'   : 'ten',
            }


translate(english, 'năm')
translate(english, 'chín mươi')
