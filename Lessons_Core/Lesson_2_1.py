# default_name = "Unknown"
# name = input("Enter your name: ")

# current_name = name or default_name
# print(current_name)




# age = int(input("How old are you?: "))
# if age >= 21:
#     print("Welcome")
# else:
#     print("You are not allowed")
# print("Thanks anyway")



# age = int(input("How old are you?: "))
# message = "Welcome" if age >= 21 else "Wrong input"
# print(message)


# age = int(input("How old are you?: "))
# print("Welcome" if age >= 21 else "Wrong input")



# print("Welcome" if int(input("How old are you?: ")) >= 21 else "Wrong input")


# i = 0
# while i < 3:
#     print("woooooooooooo!")
#     i += 1
# print("The end!")


# name = input("What is your name?: ")

# while not name:
#     name = input("What is your name?: ")
# print(f"Thanks, {name}")



# import random

# while True:
#     number = random.randint(0, 2)
#     users_number = int(input("Your number?:"))
#     if number == users_number:
#         print("You won!")
#     else:
#         print("You lost!")




# full_list = ""

# while True:
#     product = input("What you want to buy?: ")
    
#     if product == "stop":

#         print(full_list)
#         break
    
#     full_list += product + " "  


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = None

# if first < second:
#     gcd = first
    
# else:
#     gcd = second

# while first % gcd != 0 or second % gcd != 0:
#     gcd -= 1
# print(gcd)

#пока первое число не поделиться на наименьшее без остачи и второе число не поделиться на наименьшее без остачи



# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#     if 65 <= ord(ch) <= 90:
#         pos = ord(ch) - ord("a")
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message += new_char
#     elif 97 <= ord(ch) <= 122:
#         pos = ord(ch) - ord("a")
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message += new_char
#     else:
#         encoded_message += ch
# print(encoded_message)


# result = None
# operand = None
# operator = None
# wait_for_number = True
# while True:
#     if wait_for_number:
#         try:
#             operand = input("Enter operand: ")
#             operand = int(operand)
#             if result == None:
#                 result = operand
#             else:
#                 if operator == "+":
#                     result += operand
#                 elif operator == "-":
#                     result -= operand
#                 elif operator == "*":
#                     result *= operand
#                 elif operator == "/":
#                     result /= operand   
#             wait_for_number = False 
#         except ValueError:
#             print(f"{operand} is not a number. Try again")
#             continue

#     if not wait_for_number:
#         operator = input("Enter operator: ")
#         if operator == '=':
#             print(float(result))
#             break
#         elif operator != "+" and operator != "-" and operator != "*" and operator !="/":
#             print(f"{operator} is not '+' or '-' or '*' or '/'")
#             continue
#         elif operator == "+" or operator == "-" or operator == "*" or operator =="/":
#             wait_for_number = True



# while True:
#     try:
#         user_input = int(input("Enter yout age: "))
#     except ValueError:
#         print("Incorrect value, should be a nubmer")
#     else:
#         break

# current_year = 2023
# birth_year = current_year - user_input
# print(f"You born at {birth_year}")




# result = 0
# first = 1
# position = 25
# for _ in range(0, position):
#     result, first = first, result + first
# print(result)



# product_count = 20
# speed = 5
# hours_passed = 0

# while product_count > 0 and speed > 0:
#     product_count -= speed
#     speed -= 1
#     hours_passed += 1
# print(hours_passed)

# while True:
#     try:
#         num = int(input("Enter your number: "))
#         if num % 2 == 0:
#             print(f'Your number - {num} is even')
#         else:
#             print(f'Your number - {num} is odd')
#     except ValueError:
#         print("You should enter a number")
#         continue



# d = input('take day: ')
# m = input('take month: ')
# y = input('take year: ')

# try:
#     d = int(d)
#     m = int(m)
#     y = int(y)
# except ValueError as e:
#     print(e)

# if m < 0 or m > 12:
#     raise ValueError('Month must be from 1 to 12')
# if m in (1, 3, 5, 7, 8, 10, 12):
#     if d <=0 or d > 31:
#         raise ValueError('Day should be between 1 and 31')
# elif m in (4, 6, 9, 11):
#     if d <=0 or d > 30:
#         raise ValueError(f'In month {m} Day should be between 1 and 30')
# else:
#     if y % 400 == 0:
#         isLeapYear = True
#     elif y % 100 == 0:
#         isLeapYear = False
#     elif y % 4 == 0:
#         isLeapYear = True
#     else:
#         isLeapYear = False
    
#     if isLeapYear:
#         if d <=0 or d > 29:
#             raise ValueError(f'In month {m} between 1 and 29')
#     else:
#         if d <=0 or d > 28:
#             raise ValueError(f'In month {m} between 1 and 28')

# print(f'{d}.{m}.{y}')




# side_1 =  float(input('First side: '))
# side_2 =  float(input('Second side: '))
# side_3 =  float(input('Third side: '))

# if side_1 == side_2 and side_2 == side_3:
#     print('Рівносторонній')
# elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
#     print('Рівнобедренний')
# else:
#     print('Різносторонній')



# user_input = input('Take string: ')

# if not user_input:
#     print('Nothing entered')

# count_ch = 0

# for ch in user_input:
#     if ch == 'a':
#         count_ch += 1

# print(f'{count_ch}')




# deposit = 100
# percent = 0.05
# period = 10
# old_deposit = deposit

# for i in range (0, period):
#     new_deposit = deposit * (1 + percent / 12) ** 12
#     deposit = new_deposit

# profit = deposit - old_deposit
# print(profit)


