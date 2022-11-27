# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in [False, True]:
    for y in [False, True]:
        for z in range(0, 2):
            print(not (x or y or z) == (not x and not y and not z))