month = dict()

month['1'] = 'Зима'
month['2'] = 'Зима'
month['3'] = 'Весна'
month['4'] = 'Весна'
month['5'] = 'Весна'
month['6'] = 'Лето'
month['7'] = 'Лето'
month['8'] = 'Лето'
month['9'] = 'Осень'
month['10'] = 'Осень'
month['12'] = 'Осень'
month['12'] = 'Зима'

print('Введите название месяца: ')

Seasons = input()
if Seasons in month:
    print('Время года вашего месяца: ', month[Seasons])
    