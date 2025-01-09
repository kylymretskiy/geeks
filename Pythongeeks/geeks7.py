# lambda функции. Обработка исключений

# lambda1 = lambda n1, n2: n1 + n2
# print(lambda1(2, 3))
#
# def def1(n1,n2):
#     return n1 + n2
# print(def1(2,3))

# def up_first_letter(word: str) -> str:
#     return word.title()
#
# def show_words(func, objects):
#     for i in objects:
#         print(func(i))
#
# show_words(lambda word: word.title(), ['kemin', 'kara-balta', 'osh'] )
# #
# words = ['tokmok', 'karakol', 'kant']
# show_words(up_first_letter, words)

cities = ['bishkek' , 'jalal-abad', 'nookat', 'cholpon-ata' , 'kemin']
sorted_cities = sorted(cities, key=lambda word: word[-1])
filter_cities =  list(filter(lambda word: '-' not in word, cities))
map_cities = tuple(map(lambda word:word.upper(), cities))

print(sorted_cities,filter_cities,map_cities, sep='/n')
# cities = [i.upper() for i in cities if '-' not in i]
# print(cities)

# try:
#     print(2 - 'kg')
# except:
#     print('нашли ошибку')
# else:
#     print("проверка прошла успешно")
# finally:
#     print("проверка завершена")

