import math

n = int(input("podaj rozmiar macierzy: "))

matrix = [['+' if math.gcd(i + 1, j + 1) == 1 else '.' for j in range(n)] for i in range(n)]

for row in matrix:
    for el_kol in row:
        print(el_kol, end=" ")
    print()