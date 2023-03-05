# """Lists"""

# lst = []

# lst1 = [1, 2, 3, 4]

# lst2 = list()

# lst3 = [i for i in range(10)]

# print(lst3)


# # lst3.clear()

# num1 = lst3[1]
# print(num1)


# for i in lst3:
#     print(i)

# word = 'Hello'

# lst_chr = []

# for i in word:
#     lst_chr.append(i)

# print(lst_chr)


# lst3.remove(3)  # видаляє за значенням

# print(lst3)

# lst3.insert(1, 'D')  # вставляэ за індексом
# print(lst3)

# lst3.extend(['w', 'e'])
# lst3 += 'World'  # same as extend
# print(lst3)


from pathlib import Path
import sys
import pathlib
import os
text = 'Hello world'
ch = 'l'


# def count(text, ch):

#     count = 0
#     for i in text:
#         if i == ch:
#             count += 1
#         else:
#             continue
#     print(count)


# count(text, ch)


# def indexex_ch(text: str, ch: str) -> tuple[list[int], str, int]:
#     result = []
#     for index, element in enumerate(text):
#         if element == ch:
#             result.append(index)
#     return result, ch, len(result)


# if __name__ == '__main__':
#     result = indexex_ch(text, ch)
#     print(f'In text symbol {result[1]}, find {result[2]} times')


"""dict"""

# dct1 = {}
# dct2 = dict()
# dct3 = {str(i): i**2 for i in range(10)}

# print(dct1)
# print(dct2)
# print(dct3)


# print(dct3.keys())
# print(dct3.values())
# print(dct3.items())


# print(dct3['4'])

# try:
#     print(dct3.get('10'))  # не викликає помилку якщо ключа немає
# except KeyError as e:
#     print(f'Key {e} not in dcit')


# dct3.update({10: 10**2})

# print(dct3)

# dct3.update(last=100**2)
# print(dct3)


# lst = [i for i in range(10)]


# def odd_even(lst):
#     result = {'odd': [], 'even': []}
#     for i in lst:
#         if not % 2:
#             result['even'].append(i)
#         else:
#             result['odd'].append(i)
#     return result


# if __name__ == '__main__':
#     print(odd_even(lst))


# dct = {'Bill': '12345678', 'Jill': '4564465', 'Dill': '4545654'}


# def find_contact(dct, number):
#     result = []

#     for name, phone in dct.items():
#         if str(number) in phone:
#             result.append((name, phone))
#     return result


# if __name__ == '__main__':
#     print(find_contact(dct, 2))


contact_list = [{'name': 'Bill', 'phones': ['6546458', '572135']},
                {'name': 'Jill', 'phones': ['1235456', '574597']}]


# def find_contact(contacts, number=1):
#     result = None
#     for contact in contacts:
#         phones = contact['phones']
#         for phone in phones:
#             if str(number) in phone:
#                 if not result:
#                     result = [contact]
#                 else:
#                     result.append(contact)

#     return result


# def find_contact(contacts, number):
#     result = []
#     for contact in contacts:
#         if str(number) in str(contact):
#             result.append(contact)
#     return result


# if __name__ == '__main__':
#     print(find_contact(contact_list, 45))


"""SET"""

# set1 = set()

# set2 = {1, 2}

# set3 = set('abagalamaga')
# print(set3)

# set4 = set([(1, 2), (3, 5)])

# print(set4)


# lst1 = ['hello', 'world', 'word', 'hello']


# def has_doubles(lst):
#     if len(lst) == len(set(lst)):
#         return False
#     return True


# if __name__ == '__main__':
#     print(has_doubles(lst1))


"""Pathlib"""


# print(os.path.exists('D://Games'))

# path = pathlib.Path(r'D:/Games')

# print(type(path))

# print(path.exists())

# for i in path.iterdir():
#     print(f'{i.name} - {i.is_dir()}')


"""argv"""


# try:
#     path = Path(sys.argv[1])
#     print(path.exists())
# except IndexError as e:
#     print(f'Sorry. No parametr')
