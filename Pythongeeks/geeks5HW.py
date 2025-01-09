# Дан словарь, состоящий из основных данных нашего учебного заведения:
#
#
# Geeks = {
#     'address': 'Toktogula 175',
#     'courses': ['Android', 'Backend', 'Frontend'],
#     'bag': {'fails', 'errors', 'stack'}
# }
#
#
# Удалить bag
#
# Изменить старый адрес на нынешний
#
# Добавить номер телефона и инстаграмм аккаунт Geeks
#
# Добавить/расширить список актуальными курсами, которые вы знаете. Затем преобразовать этот список в set
#
# Добавить дату основания Geeks в виде строки
#
# Вывести количество курсов
#
# Вывести словарь на экран с помощью цикла for с получением всех пар
# “ключ: значение”


geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
geeks.update({'number' : +996700666550, 'insta': 'geeks_edu'})
geeks.pop('bag')
geeks['address'] = 'Ibragimova 103'
geeks['courses'] = {'Android', 'Backend', 'Frontend' , 'ux/ui'}
geeks['date'] = '2018'


print('Кол-во курсов: ', len(geeks['courses']))
for key,value in geeks.items():
    print(f'{key}: {value}')

