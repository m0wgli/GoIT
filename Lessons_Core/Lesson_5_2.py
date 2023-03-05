"""gallows"""

gallows = [[' ', '-', '-', '-', '-', '-'],
           [' ', '|', ' ', ' ', ' ', '|'],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           ['/', ' ', '\\', ' ', ' ', ' ']]

# print('\n'.join([''.join(ch) for ch in gallows]))


word = 'pizza'

# print('_' * len(word))

answer_word = ['_' for _ in range(len(word))]

# print(('_ ' * len(word)).rstrip())

print(' '.join(answer_word))


while ''.join(answer_word) != word:

    user_input = input('Type your letter >>>')

    if user_input in word:
        letter_index = word.find(user_input)
        answer_word[letter_index] = user_input
        print(' '.join(answer_word))
