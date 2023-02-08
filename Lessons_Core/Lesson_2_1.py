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



while True:
    try:
        user_input = int(input("Enter yout age: "))
    except ValueError:
        print("Incorrect value, should be a nubmer")
    else:
        break

current_year = 2023
birth_year = current_year - user_input
print(f"You born at {birth_year}")
