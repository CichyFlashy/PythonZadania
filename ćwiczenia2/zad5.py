from random import randint

def reverse_matrix(matrix):
     reversed_matrix = [x[::-1] for x in matrix]
     reversed_matrix.reverse()
     return reversed_matrix

n = int(input("Podaj rozmiar macierzy: "))
a = int(input("Podaj początkowy zakres macierzy: "))
b = int(input("Podaj końcowy zakres macierzy: "))

matrix = [[randint(a,b) for _ in range(n)] for _ in range(n)]

sum_of_first_diagonal = 0
for i in range(n):
    sum_of_first_diagonal += matrix[i][i]

for row in matrix:
    for el_kol in row:
        print(el_kol, end=" ")
    print()

print("Suma pierwszej przekątnej wynosi: ", sum_of_first_diagonal)

sum_of_second_diagonal = 0
for i, y in zip(range(n), range(n-1, -1, -1)):
    sum_of_second_diagonal += matrix[i][y]

print("Suma drugiej przekątnej: ", sum_of_second_diagonal)

sum_of_odd_positions = 0
for i in range(n):
    if i % 2 == 0:
            continue
    else:
        for y in range(n):
                if y % 2 == 0:
                    continue
                else:
                    sum_of_odd_positions += matrix[i][y]

print("Suma elementów na pozycjach nieparzystych wynosi: ", sum_of_odd_positions)

reversed_matrix = reverse_matrix(matrix)
for row in reversed_matrix:
    for el_kol in row:
        print(el_kol, end=" ")
    print()
