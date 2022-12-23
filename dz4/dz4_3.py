# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
import random

lst = [random.randint(0, 9) for i in range(random.randint(7, 15))]
print(lst)
lst1 = []
lst2 = lst.copy()
for i in range(0, len(lst)):
    lst2.pop(i)
    if lst[i] not in lst2:
        lst1.append(lst[i])
    lst2 = lst.copy()
print(lst1)
