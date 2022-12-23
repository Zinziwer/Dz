# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 14x^8 +30x^7 -9x^6 -13x^5 -58x^4 -25x^3 +90x^2 -60x +74  = 0
# 8x^4 +9x^3 -65x^2 -75x +94  = 0
with open('uravn.txt', 'r') as x:
    y1 = x.readline()
    y2 = x.readline()
print(y1, y2)


def koef1(y: str) -> list:
    y = y.replace('+', ' ')
    y = y[:-4].split()
    return y


y3 = koef1(y1)
y4 = koef1(y2)

print(y3, y4)


def dictionario(y: list) -> dict:
    y400 = []
    for i in y:
        if not 'x' in i:
            y400.append([i, 0])
        else:
            if i[-1] == 'x':
                if i == 'x':
                    y400.append([1, 1])
                elif i == '-x':
                    y400.append([-1, 1])
                else:
                    y400.append((i + '1').split('x'))
            else:
                if i[0] == 'x':
                    y400.append(('1' + i).split('x^'))
                elif i[0] == '-x':
                    y400.append(i.replace('-', '-1').split('x^'))
                else:
                    y400.append(i.split('x^'))
    y_dict = {}
    for i in y400:
        y_dict[int(i[1])] = int(i[0])
    return y_dict

y5 = dictionario(y3)
y6 = dictionario(y4)
print(y5,y6)