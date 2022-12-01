# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number1 = int(input('введите число '))
d = ''
while number1 > 0:
    d = str(number1 % 2) + d
    number1 //= 2
print(d)
