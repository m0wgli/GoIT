"""Методи рядків"""

# text = 'hello world'

# print(text.capitalize())

# print(text.title())

# print(text.upper())

# print(text.lower())

# print(text.find('l'))


# def find_all(text: str, substring):
#     result = []
#     start_position = 0
#     for i in range(len(text)):
#         position = text.find(substring, start_position)
#         if position > - 1:
#             result.append(position)
#             start_position = position + 1
#     return result


# print(find_all(text, 'l'))


"""replace"""

# text = 'I love Python'

# print(text.replace(' ', '\n').replace('I', 'You'))


"""Split"""

# text = 'Hello. World. Sun.'

# result = []

# for i in text.strip('.').split('.'):
#     i = i.strip()
#     result.append(i)

# print(result)


"""Startwith, removesuffics"""

# text = 'hello world'

# print(text.startswith('hello'))
# print(text.endswith('world'))

# print(text.removeprefix('hello').strip())
# print(text.removesuffix('world').strip())


"""Translate"""

# text = 'ПрПрПрПрПрПрПр'

# for i in text:
#     print(ord(i))

# print(text.translate({1055: 'H', 1088: 'e'}))


"""Format"""

# print(f'{1+1}{2+2}{3+3}')

# print('{:^10}{:<10}{:>10}'.format(12, 12, 12))


# print('{0:d}|{0:#x}|{0:#o}|{0:#b}'.format(10))

# print(f'{hex(10)}')

# print('{a} {b}'.format(a='Hello', b='World'))


"""Regular expressions"""


# import re
# text = '''Sit amet quis 156 labore gubergren sed est aliquyam duis
#     labore est eu consequat kasd elit voluptua ut lorem lorem.
#     No vero invidunt. Eirmod accusam 84 eos no eos elitr consequat
#     facer clita autem lorem duo molestie in invidunt est et dolores.
#     Vero tation diam magna ad ut'''

# amet = re.search('amet', text)

# print(amet.span())

# digit = re.findall(r'\d+', text)

# print(digit)

# text1 = 'blue blue blue'

# sub_string = re.sub(f'amet|quis|sed|est', 'bad word', text)

# print(sub_string)

# user_input = input('>>>')

# sub1 = re.sub(fr'{user_input}', 'bad word', text1)

# print(sub1)


# def find_word(text, word):
#     search_result = re.search(word, text)
#     if search_result:
#         return {
#             'result': True,
#             'first_index': search_result.start(),
#             'last_index': search_result.end() - 1,
#             'search_string': search_result.group(),
#             'string': text
#         }
#     else:
#         return {
#             'result': False,
#             'first_index': None,
#             'last_index': None,
#             'search_string': word,
#             'string': text
#         }


# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))




import re
def replace_spam_words(text, spam_words):
    result = text
    spam = ''
    for word in spam_words:
        spam += f'{word}|'
    return re.sub('(' + spam + ')', '*'*len(word), text, flags=re.IGNORECASE)


replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', [
                   'began', 'Python'])
