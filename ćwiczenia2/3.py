import random

matrix = [[random.randint(-5, 5) for _ in range(5)] for _ in range(5)]

for row in matrix:
    for el_kol in row:
        print(el_kol, end=" ")
    print()

for i in range(5):
    min = matrix[0][i]
    max = matrix[0][i]
    for j in range(5):
        if matrix[j][i] > max:
            max = matrix[j][i]
        if matrix[j][i] < min:
            min = matrix[j][i]
    print(f"Maksimum dla kolumny nr {i + 1} wynosi: {max}")
    print(f"Minimum dla kolumny nr {i + 1} wynosi: {min}")
    




