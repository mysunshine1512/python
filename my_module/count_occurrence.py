def count_occurrence(text, words_count):
    occurrence = []
    for word in text:
        if word == words_count:
            occurrence.append(words_count)
    print('Number of occurrence of {} in a {} is: {}'.format(words_count, text, len(occurrence)))

# Test code
text = input('Enter your text: ')
words_count = input('Enter the word you want to count: ')
count_occurrence(text, words_count)