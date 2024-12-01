def obl_wiel(x: float, n: int, *coeffs: float) -> float:
    wynik = 0
    for i, coeff in enumerate(coeffs):
        wynik += coeff * (x ** i)
    return wynik


print(obl_wiel(4, 2, 1, 2, 3))  
print(obl_wiel(3, 3, 5, -2, 0, 4))  