# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N. (Выполнили на семинаре)
# задайте 2 числа. ищем НОК и НОД
from Func import functions

a, b = int(input('первое ')), int(input('второе '))
s1 = functions.mnoziteli(a)
s2 = functions.mnoziteli(b)
s3 = []
for i in s1:
    for j in s2:
        if i == j:
            s3.append(i)
if len(s3) == 0:
    print('НОД отсутствует')
    print(f'НОК {round(a * b)}')
else:
    print(f'НОД {max(s3)}')
    print(f'НОК {round(a * b / max(s3))}')
# решение для НОД, сделанное на семинаре не рабочее для делителей типа 4(2*2) или 9(3*3) ..., если что)
