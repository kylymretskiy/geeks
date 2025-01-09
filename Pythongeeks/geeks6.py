# Функции: виды параметров, возвращение данных, виды аргументо.
#DRY - don't repeat yourself
# def -define

"""из чего состоит функция"""
# определение наименования(параметры):
#     тело Функции
#     возвращение объекта(результата)
#
# вызов функции
# наименование(аргументы)
#
# def some_function(name):
#     print('hello')
#
# some_function()

# def some_function(name, surname='неизвестно'):
#     print(f'name: {name} surname: {surname}')
#
#
# some_function('adilet',  'tairov')
# some_function(surname='tyson', name='mike')
# some_function('chyngyz')

# def get_square(length: int, width: int) -> int:
#     """Принимает длину и ширину. Возвращает площадь"""
#     square = length * width
#     return square
#
# print(help(get_square))
# print(get_square.__doc__)
# print(get_square.__annotations__)



# square_2 = get_square(7, 5)
# square_victory = get_square(350, 110)
# square_hall = get_square(
#     length=int(input('enter length: ')),
#     width=int(input('enter width: '))
# )
#
# print(square_victory, square_hall, square_2, sep='\n')

# length = 7
# width = 5
# square_2 = length * width
# print(square_2)
#
# length = 110
# width = 350
# square_3 = length * width
# print(square_3)

# def menu(**kwargs):
#     return kwargs
#
# monday = menu(eat = "pizza" , drink = "cola")
# print(monday)
# #
# def plus(*args):
#     return sum(args), args[0]
#
# print(plus(1,2,3,4))
# print(plus(215,267,8739,54))

# numbers = [41, 225, 53,76, 64,85]
# min_val = numbers[0]
#
# for number in numbers:
#     if number > min_val:
#     min_val = number
#
# print(min_val)


# max.__doc__
#
# print(max.__doc__)
