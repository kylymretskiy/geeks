# def nearest_number(numbers, target):
#     sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
#     return target, sorted_numbers
#
#
# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# target = int(input("Введите целевое число: "))
#
# result = nearest_number(numbers, target)
# filter_number =list(filter(lambda x:x > target, numbers ))
# map_number = tuple(map(lambda x: x +23, numbers))
#
# print(result , filter_number, map_number)

# def get_element(iterable=[1, 2, 3, 4, 5]):
#     while True:
#         try:
#             index = input(f"Введите индекс (доступные от 0 до {len(iterable) - 1}) или 'exit' для выхода: ")
#
#             if index.lower() == 'exit':
#                 break
#             index = int(index)
#             print(f"Элемент с индексом {index}: {iterable[index]}")
#
#         except ValueError:
#             print("Ошибка: Введите целое число или 'exit' для выхода.")
#         except IndexError:
#             print(f"Ошибка: Индекс вне диапазона. Допустимые индексы от 0 до {len(iterable) - 1}.")
#
# get_element()



