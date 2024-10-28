import math

a = int(input("Podaj początkowy zakres liczb: "))
b = int(input("Podaj końcowy zakres liczb: "))
numbers = [(x, math.pow(2, x), math.sqrt(x)) for x in range(a, b+1) if x % 2 != 0 ]

for number in numbers:
    print(number)
