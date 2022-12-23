def input_int(text: str, error: str) -> int:
    while True:
        try:
            number = int(input(text))
            return number
        except:
            print(error)


def mnoziteli(a: int):  # разложение числа на множители
    ddd = []
    for i in range(2, a//2 + 1):
        if a % i == 0:
            ddd.append((i))
    ddd.append(a)
    return ddd
