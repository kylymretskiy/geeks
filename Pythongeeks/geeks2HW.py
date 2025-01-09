date = int(input('введите дату рождения: '))
month = int(input('введите месяц рождения: '))
if month == 1 and 21 <= date <= 31:
    print('водолей')
elif month == 2 and 1 <= date <= 19:
    print('водолей')
elif month == 2 and 20 <= date <= 28:
    print('рыба')
elif month == 3 and 1 <= date <= 20:
    print('рыба')
elif month == 3 and 21 <= date <= 31:
    print('овен')
elif month == 4 and 1 <= date <= 20:
    print('овен')
elif month == 4 and 21 <= date <= 30:
    print('телец')
elif month == 5 and 1 <= date <= 21:
    print('телец')
elif month == 5 and 22 <= date <= 31:
    print('близнецы')
elif month == 6 and 1 <= date <= 21:
    print('близнецы')
elif month == 6 and 22 <= date <= 30:
    print('рак')
elif month == 7 and 1 <= date <= 22:
    print('рак')
elif month == 7 and 23 <= date <= 31:
    print('лев')
elif month == 8 and 1 <= date <= 21:
    print('лев')
elif month == 8 and 22 <= date <= 31:
    print('дева')
elif month == 9 and 1 <= date <= 23:
    print('дева')
elif month == 9 and 24 <= date <= 30:
    print('весы')
elif month == 10 and 1 <= date <= 23:
    print('весы')
elif month == 10 and 24 <= date <= 31:
    print('скорпион')
elif month == 11 and 1 <= date <= 22:
    print('скорпион')
elif month == 11 and 23 <= date <= 30:
    print('стрелец')
elif month == 12 and 1 <= date <= 22:
    print('стрелец')
elif month == 12 and 23 <= date <= 31:
    print('козерог')
elif month == 1 and 1 <= date <= 20:
    print('козерог')
else:
    print('укажите правильно др!')
