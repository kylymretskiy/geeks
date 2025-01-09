from Pythongeeks.geeks3HW import count


# def game():
#     user_chislo = int(input('Загадайте число от 1 до 100. Программа будет угадывать его: '))

#     # Проверка корректности ввода
#     if user_chislo < 1 or user_chislo > 100:
#         print('Ошибка! Введите число от 1 до 100.')
#         game()
#
#     counter = 0
#     chislo = 50
#     low, high = 1, 100  # Диапазон значений
#
#     while True:
#         counter += 1
#         print(f'Ваше число {chislo}? (да/больше/меньше)')
#         user_input = input().strip().lower()
#
#         if user_input == 'да':
#             print(f"Угадал число {chislo} за {counter} попыток!")
#             break
#         elif user_input == 'больше':
#             low = chislo + 1  # Сужаем диапазон снизу
#             chislo = (low + high) // 2
#         elif user_input == 'меньше':
#             high = chislo - 1  # Сужаем диапазон сверху
#             chislo = (low + high) // 2
#         else:
#             print("Пожалуйста, введите 'да', 'больше' или 'меньше'. Попробуйте снова.")
#
#         # Проверка выхода за границы диапазона
#         if low > high:
#             print('Ошибка! Диапазон выходит за пределы. Начнем заново.')
#             restart = input("Хотите начать новую игру? (да/нет): ").strip().lower()
#             if restart == 'да':
#                 game()  #
#             else:
#                 print("Спасибо за игру!")
#             break
#
# with open('save_results.txt', 'w') as file:
#     file.write(f'количество попыток: {count}')
#
# with open('save_results.txt', 'a') as file:
#     file.write(f'\nсписок попыток: ')
#
# with open('save_results.txt', 'a') as file:
#     file.write(f'\nзагаданное число: ')
#
# game()

def calculator(num1: float, operator: str, num2: float) -> float:

    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Оба числа должны быть числами.")

        # Выполнение операции в зависимости от оператора
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '**':
            return num1 ** num2
        else:
            raise ValueError("Недопустимый оператор. Используйте +, -, *, /, %, **.")
    except (ZeroDivisionError, ValueError, TypeError) as e:
        return f"Ошибка: {e}"

# Пример использования:
print(calculator(10, '+', 5))   # 15
print(calculator(10, '/', 0))   # Ошибка: Деление на ноль невозможно.
print(calculator(10, 'x', 5))   # Ошибка: Недопустимый оператор.
print(calculator("10", '+', 5)) # Ошибка: Оба числа должны быть числами.
