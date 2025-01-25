# summa = []
# summa_2 = 0
#
# for i in range(1, 1001):
#     summa.append(i)
#
# for j in summa:
#     if j % 2 == 0 or j % 3 == 0:
#         summa_2 += j
#         print(j)
#
# print(summa_2)


# user = input('What is your name? ')
# year = int(input('How old are you? '))
#
# if year >= 18:
#     print(f'Hello, {user}')
#     print f'You are {year} years old')
#
# elif year < 18:
#     print('Call one of your parents')
#     p_user = input('What is your name? ')
#     p_year = int(input('How old are you? '))
#
#     if p_year >= 18:
#         print(f'Hello, {p_user}')
#         print(f'You are {p_year} years old')
#
#     elif p_year < 18:
#         print('I said call your parents!'


# username = input('Enter user: ')
# password = input('Enter password: ')
#
# username_check = input('Enter your registered username: ')
#
# if username_check == username:
#     password_check = input('Enter your registered password: ')
#     while password_check != password:
#         password_check = input('Enter your password: ')
#         if password_check == password:
#             print('Welcome')

# a = input('Hi, how are you? ')
# if a == 'good':
#     print('Im glad youre okay.')
#     c = input('what are your hobbies? ')
#     print('thats cool!')
#     d = input('do you have favourite food? ')
#     print('sounds tasty.')
#     e = input('what about color? ')
#     print('oh, i like it too.')
#     f = input('whats your favorite sport? ')
#     print('i saw it few times on tv.')
#     g = input('do you like animals? ')
#     if g == 'yes':
#         h = input('who do you like more, cats or dogs? ')
#         print('theyre cuties, arent they?')
#     elif g == 'no':
#         i = input('why? ')
#         print('oh, okay.')
# elif a == 'not good':
#     b = input('you can tell if something bothering you. ')
#     print('dont worry! everything will be okay.')



# equation = input("write a problem: ")
#
# number_1 = int(equation[0])
# number_2 = int(equation[2])
# operation = equation[1]
#
# def calculator(num1, num2, operation):
#     if operation == '+':
#         print(num1 + num2)
#
#     elif operation == '-':
#         print(num1 - num2)
#
#     elif operation == '*':
#         print(num1 * num2)
#
#     else:
#         print(num1 / num2)


# число фибоначчи. Человек вводит номер, а программа выдает число фибоначчи под этим номером

# def fibonacci(index):
#     list = [1, 1]
#     ind = 0
#     print(list)
#     while index > len(list):
#         ind += 1
#         list.append(list[ind-1] + list[ind])
#         print(ind)
#         print(index)
#         print(list)
#         if ind == (index-2):
#             return list[-1]
#
#
# print(fibonacci(int(input())))



# вводишь число возвращается его номер

# def fibonacci(chislo):
#     list = [1, 1]
#     ind = 0
#     for i in list:
#         ind += 1
#         list.append(list[ind-1] + list[ind])
#         if i == chislo:
#             return ind
#
#
# print(fibonacci(int(input())))


# камень, ножницы, бумага. йее эщкере

# import random
#
# player = int(input("Enter: 1 - paper, 2 - rock, 3 - scissors "))
# computer = random.randint(1,3)
# print(computer)
#
# if player == 1 and computer == 1 or player == 2 and computer == 2 or player == 3 and computer == 3:
#     print('Draw!')
#
# elif player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
#     print('You win!')
#
# elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
#     print('You lose!')
#
# else:
#     print('Error')












# ЭХО БОТ

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     bot.send_message(message.chat.id, message.text)








# ТЕСТ ФУНКЦИЙ ТЕЛЕБОТА

# @bot.message_handler(commands=["start"])
# def start(message):
#     mess = f'hello broooo {message.from_user.first_name}'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
# @bot.message_handler(commands=['btns'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("<3", url="https://www.instagram.com/hollyfxe?igsh=MXd3NWV4czRvZG1tcg=="))
#     bot.send_message(message.chat.id, "FOLLOW ME POOKIE", reply_markup=markup)
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup()
#     website = types.KeyboardButton('/btns')
#     start  = types.KeyboardButton('/start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "FOOOL", reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "hello":
#         bot.send_message(message.chat.id, "OH, HALLO, MY FRIEND", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"your id: {message.from_user.id}", parse_mode='html')
#     elif message.text == "pic":
#         photo = open("WhatsApp Image 2024-06-04 at 13.22.56.jpeg", "rb")
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "WHATCHA SAYING?", parse_mode='html')
#
#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, "IT LOOKS LIKE A CRAP, LOOOOOSER")




