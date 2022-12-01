# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('введите число '))
a = 0
b = 1
c = 0
d = -1
fib = []
neg = []
for i in range(n):
    fib.append(a)
    a, b = b, a + b
for i in range(n - 1):
    c, d = -d, -(c + d)
    neg.append(c)
neg.reverse()
print(*neg, end=' ')
print(*fib)
