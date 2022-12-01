# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
import random

lst2 = []
lst = [round(random.random() * 10, 2) for i in range(random.randint(3, 8))]
print(lst)
for i in lst:
    lst2.append(round(i - int(i), 2))
print(lst2)
print(f'разницa между максимальным и минимальным значением дробной части элементов: {round(max(lst2) - min(lst2), 2)}')
