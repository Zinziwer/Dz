# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*
import random

k = int(input('Введите порядок уравнения '))
fin = ''
koef = [str(random.randint(-100, 100)) for i in range(k + 1)]
print(koef)
for i in range(len(koef)):
    if koef[i] == '1':
        fin += '+ x^' + str(k - i) + ' '
    elif koef[i] == '-1':
        fin += '- x^' + str(k - i) + ' '
    elif koef[i] != '0':
        fin += '+ ' + koef[i] + 'x^' + str(k - i) + ' '
if koef[k] == '-1' or koef[k] == '1':
    fin = fin[:-1] + '1'
fin = fin.replace('x^0', '') + ' = 0'
fin = fin.replace('x^1', 'x')
fin = fin.replace('+ -', '- ')
if fin[0] == '+':
    fin = fin[1:]
print(fin)
with open('uravn.txt', "a") as x:
    x.write(fin)
    x.write('\n')
# Все вроде бы работает, кроме порядка  более 9 и  все х = 0
