# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

# d = {i: round((1 + 1 / i) ** i, 2) for i in range(1, int(input()) + 1)}
# print(d)
# print (sum(d.values()))
print(sum({i: round((1 + 1 / i) ** i, 2) for i in range(1, int(input('введите N ')) + 1)}.values()))
