# lst2 = []
# lst1 = ['1', 10, lst2]

# for i in lst1:
#     print(type(i))

# for i in range(len(lst1)):
#     print(lst1[i])


# lst1 = [str(i) for i in range(10)]

# print(lst1[0:3:2])

# print(lst1[::-1])


# lst2d = [[2, 3, 4],
#          [5, 6, 7],
#          [8, 9, 0]]

# print(lst2d[0][0])
# print(lst2d[1][1])


# lst1 = [[], []]

# for i in range(10):
#     lst1[1].append(i)

# print(lst1)

# lst1.clear()
# print(lst1)


# lst2 = [str(i) for i in range(10)]

# # lst2.remove('8')
# # print(lst2)

# print(lst2.pop())
# print(lst2)


# for i in range(10):
#     print(lst2.pop())


# lst3 = [10, 20, 30]
# lst2.extend(lst3)

# print(lst2 + lst3)


# lst2.append(lst3.pop())
# print(lst2)


# lst3.insert(1, 40)
# print(lst3)


# lst1 = ['a', 'b', 'a', 'c', 'A']
# print(lst1.count('a'))

# lst1.sort()
# print(lst1)

# lst1.reverse()
# print(lst1)


"""Dict"""


# dct1 = {}
# dct2 = dict()

# print(type(dct1), type(dct2))


# dct1['key1'] = 'Value1'
# print(dct1)

# dct1['key1'] = 'Value2'
# print(dct1)

# dct3 = {(1, 2): 'List1'}
# print(dct3)


# dct4 = {str(i): i for i in range(10)}
# print(dct4)


# dct1 = {f'key-{i}': i for i in range(10)}

# for i in dct1:
#     print(f'{i}: {dct1[i]}')

# for k, v in dct1.items():
#     print(f'{k} : {v}')


# person = {'name': 'Bill', 'age': 30}

# print(person.get('address', 'Not set'))

# print(person.get('name', 'Not set'))

# address = person.get('address', 'Not set')
# name = person.get('name', 'Not set')

# if address < 0:
#     print('Address not set')

# print(person.pop('name'))
# print(person)

# person.update({'name': 'Jill'})
# print(person)

# person['weight'] = 76
# print(person)


# if not person.get('height'):
#     person['height'] = 200

# person['dogs'] = ['Patron']


# person['dogs'].append('Bobik')

# dogs = person['dogs']

# dogs.append('Bobik')

# person['dogs'] = dogs

# print(person)


# my_set = set('hello')

# print(my_set)

# set1 = set('hello')
# set2 = set('aloha')

# print(set1.difference(set2))

# if len('hello') != len(set('hello')):
#     print('double')

# print(set1 ^ set2)


"""String"""

# my_srt = 'Hello'
# new_str = ''
# print(my_srt[1])

# for i in my_srt:
#     if i == 'e':
#         new_str += 'b'
#     new_str += i
# print(new_str)
