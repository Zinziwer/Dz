# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

lst = [random.randint(0, 21) for i in range(random.randint(3, 8))]
print(lst)
res = []
l = len(lst)
for i in range(l // 2):
    res.append(lst[i] * lst[l - 1 - i])
if l % 2 != 0:
    res.append(lst[l // 2] ** 2)
print(res)
