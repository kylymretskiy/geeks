# Операторы: принадлежности , назначния. Циклы.

"""Оператор принадлежности"""

# print(2 in range(1,11))
# print(42 in range(1,11))
# print('p' in 'geeks')
# print('p' in 'python')

"""Операторы назначния"""

# number = 5
# number += 3 #8
# number -= 1 #7
# number *= 2  #4
# number //= 2  #7
# number **= 2  #49
# number %= 2  #1
# number /= 2  #0.5
# print(number)

"""Оператор цикла while"""

# rounds = 0
#
# while rounds < 100:
#     rounds += 1
#     if rounds == 50:
#         print('stop')
#         break
#     if rounds % 2 == 0:
#         continue
#     print('hello world', rounds)

# counter = 10
# while counter > 0:
#     print(f'сколько попыток осталось: {counter}')
#     time = input('укажите время суток: ').lower()
#     if time == 'stop':
#         break
#     if time == 'morning' or time == 'утро' :
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello! (время суток не распознано)')
#     counter -= 1

"""Оператор цикла for"""
#
# word = 'KYRGYZSTAN'
#
# for letter in word:
#     if letter == 'S':
#         break
#     if letter in 'YRZ':
#         continue
#     print(letter)

# rates = 0
# students = 14
#
# for student in range(1, students+1):
#     answer = int(input(f'enter sum rates students #{student}: '))
#     rates += answer
#     print(rates)
#
# print(rates/students)

