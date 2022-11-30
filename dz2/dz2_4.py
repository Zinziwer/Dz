# [-N, N]. Найдите произведение элементов на указанных
# позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('введите число '))
s = []
pr = 1
t = []
for i in range(-n, n + 1):
    s.append(i)
print(*s)
numb = []
x = open('file.txt')
t = x.readlines()
x.close()
t = " ".join(map(str, t))
for i in t:
    if i.isdigit():
        numb.append(i)
print(numb)
for i in numb:
    pr *= s[int(i) - 1]
print(f'Произведение элементов с номерами из файла = {pr}')
