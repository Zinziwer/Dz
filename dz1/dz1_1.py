# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
a = int(input('введите номер дня недели '))
if a == 6 or a == 7:
    print('выходной')
elif a > 7 or a < 1:
    print('такого дня недели не существует')
else:
    print('будний день')

    