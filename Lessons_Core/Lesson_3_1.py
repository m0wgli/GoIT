# def hello():
#     print('Hello')

# for _ in range(10):
#     hello()




# def hello(name: str) -> str:
#     return f'Hello {name}'

# name = 'Bill'

# for n in name:
#     print(hello(n))




# name = 'Bill'

# def lower_string(text: str) -> str:
#     name = text
#     return name.lower()

# print(lower_string(name))
# print(name)



# def sum_int(num1: int, num2: int = 10, num3: int|None = None) -> int:
#     if num3:
#         return num1 + num2 + num3
#     result = num1 + num2
#     return result

# print(sum_int(1, 20))




# a, b, *c = [1, 2, 45, 78, 102]

# print(a, b, c)




# def calc_sum(num1: int = 5, *nums, **knums) -> int:
#     result = 0
#     for num in nums:
#         result += num
#     result += num1

#     for _, item in knums.items():
#         result += item

#     return result

# nums = [1, 1, 1, 1, 1]

# k_nums = {'first': 1, 'second': 2, 'third': 3}

# print(calc_sum(5, *nums, **k_nums))



# def calc_many(*nums: list[int], **knums: dict[str, int]) -> int:
#     result = 0
#     for i in nums:
#         result += i

#     for i in knums.values():
#         result += i
    
#     return result

# nums = [1, 1, 1, 1, 1]

# k_nums = {'1': 1, '2': 2, '3': 3, '4':4}

# print(calc_many(*nums, **k_nums))



# def split_str(text: str) -> list[str]:
#     result = []
#     if text:
#         for i in text:
#             result.append(i)
#     return result

# text1 = 'Hello World'
# text2 = ''

# print(split_str(text1))
# print(split_str(text2))




# def check_result(num1, num2):
#     if num1 > num2:
#         return True, num1
#     return False, num2

# n1 = 10
# n2 = 20
# n3 = 5

# result = check_result(n1, n3)

# if result[0]:
#     print('Ok')



# GRADE = {'F': 1, 'FX': 2, 'SX': 3}

# def get_grade(grade: str) -> dict[str, int]:
#     for k in GRADE:
#         if k == grade:
#             return {k: GRADE[k]}
#     return {}

# print(get_grade('FX'))



"""Рекурсія"""

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n -1)

# print(factorial(10))


# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fibonacci(n - 1) + fibonacci(n -2)

# print(fibonacci(6))





# from Lesson_1_2 import fibonacci


# print(fibonacci(15))





# from random import randint

# lst = [randint(100, 1000) for _ in range(100)]

# def get_min_max(lst, avg = 50):
#     min_num = []
#     max_num = []
#     for i in lst:
#         if i <= avg:
#             min_num.append(i)
#         else:
#             max_num.append(i)
#     return min_num, max_num

# res1, res2 = get_min_max(lst, 200)
# print(len(res1), len(res2))




# from random import randint

# def all_sum(*args):
#     result = 0
#     for i in args:
#         result += i

#     return result


# print(all_sum(*[randint(10,100) for _ in range (100)]))



