# Вычислить число ПИ c заданной точностью d
import math

pi = str(math.pi)
d = input(f'введите d в интервале 10^-1 ≤ d ≤ 10^-10: ')
print(pi)
for i in range(0, len(d)):
    print(pi[i], end="")
