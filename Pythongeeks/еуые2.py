# def calculator(num1: float, operator: str, num2: float) -> float:
#
#     try:
#         if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
#             raise TypeError("Оба числа должны быть числами.")
#
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             if num2 == 0:
#                 raise ZeroDivisionError("Деление на ноль невозможно.")
#             return num1 / num2
#         elif operator == '%':
#             return num1 % num2
#         elif operator == '**':
#             return num1 ** num2
#         else:
#             raise ValueError("Недопустимый оператор. Используйте +, -, *, /, %, **.")
#     except (ZeroDivisionError, ValueError, TypeError) as e:
#         return f"Ошибка: {e}"
#
# print(calculator(10, '+', 5))
# print(calculator(10, '/', 0))
# print(calculator(10, 'x', 5))
# print(calculator("10", '+', 5))
from importlib.metadata import pass_none

from Pythongeeks.geeks5HW import geeks

# for i in range(1,10+1):
#     if i > 7:
#         print(i)
#     else:
#         print(False)

# geeks_in = ['Bishkek','Osh','Kara-Balta','Bishkek 9mkr']
#
# geeks_in.sort()
# geeks_in = [i.upper() for i in geeks_in]
#
# geeks_in = geeks_in[::-1]
# print(geeks_in)

geeks = 2018
current = int(input('enter: '))

if (current) > 5:
    print("5 let")
else:
    pass
elif (current - geeks) in range (1,5 + 1):
    print("menshe 5 let")