
#zad.1.
while True:
    weight = input('Podaj swoją wagę: ')
    height = input('Podaj swój wzrost: ')

    if float(weight) > 0 and float(height) > 0:
        BMI = float(weight)/((float(height)/100)**2)
        if BMI < 18.5:
            print('Niedowaga')
        elif BMI > 24.9:
            print('Nadwaga')
        else:
            print('Waga prawidłowa')
        break
    else:
        print('Podano niepoprawną wartość!')
        continue


#zad.2.
while True:
    price = float(input('Podaj cenę towaru: '))
    installment_count = float(input('Podaj liczbę rat: '))

    if price >= 100 and price <= 10000 and installment_count >= 6 and installment_count <= 48:
        if installment_count <= 12:
            loan = price/installment_count * 1.025
            print(loan)
        elif installment_count >= 25:
            loan = price / installment_count * 1.05
            print(loan)
        else:
            loan = price / installment_count * 1.1
            print(loan)
        break
    else:
        print('Wprowadzono niepoprawne dane!')
        continue


#zad.3.
number = int(input('Podaj liczbę: '))
for i in range(number):
    if i % 2 != 0:
        print(i)

#zad.3.rozszerzenie
first = int(input('Podaj pierwszą liczbę: '))
second = int(input('Podaj drugą liczbę'))
for i in range(first+1, second):
    if i % 2 != 0:
        print(i)

#zad.4.
number = input('Podaj liczbę: ')
p = input('Podaj liczbę startową: ')
i = 1

while i <= int(number):
    print(i)
    i *= int(p)

#zad.5.
suma = 0
while True:
    number = int(input('Podaj liczbe: '))
    if number == 0:
        break
    else:
        suma += number

print(suma)

#zad.6. wersja z funkcjami----
suma = 0
numbers = []

while True:
    number = int(input('Podaj liczbe: '))
    if number == 0:
        break
    else:
        numbers.append(number)


print('Użytkownik podał ciąg:')
for i in numbers:
    print(i)


def min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min


def max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


suma = min(numbers) + max(numbers)
print(f'Suma: {suma}')

avg = suma/2
print(f'Srednia: {avg}')

#zad.6. bez funkcji
suma = 0
numbers = []

while True:
    number = int(input('Podaj liczbe: '))
    if number == 0:
        break
    else:
        numbers.append(number)


print('Użytkownik podał ciąg:')
for i in numbers:
    print(i)



min = numbers[0]
for number in numbers:
    if number < min:
        min = number

max = numbers[0]
for number in numbers:
    if number > max:
        max = number



suma = min + max
print(f'Suma: {suma}')

avg = suma/2
print(f'Srednia: {avg}')

#zad.7.
import random

attempt_counter = 1

level = input('Wybierz poziom trudności(1- łatwy, 2-średni, 3-trudny): ')
if level == '1':
    drawn = random.randint(1, 51)
elif level == '2':
    drawn = random.randint(1, 101)
else:
    drawn = random.randint(1,201)



while True:
    number = int(input('Podaj swoją liczbę: '))
    if number > drawn:
        print('Podałeś za dużą wartość')
    elif number < drawn:
        print('Podałeś za małą wartość')
    else:
        print('Gratulacje')
        break
    attempt_counter += 1

print(f'Liczba prób: {attempt_counter}')


#zad.8.
while True:
    number = input('Podaj liczbę całkowitą: ')
    if int(number) < 0:
        print('Podana wartość nie może być ujemna!')
    else:
        break
suma = 0

for i in number:
    suma += int(i)

suma_parzyste = 0
suma_nieparzyste = 0
licznik_parzyste = 0
licznik_nieparzyste = 0

for i in number:
    if int(i)%2 == 0:
        suma_parzyste += int(i)
        licznik_parzyste += 1
    else:
        suma_nieparzyste += int(i)
        licznik_nieparzyste += 1

print(f'Suma cyfr: {suma}')

if licznik_parzyste > 0:
    srednia_parzyste = suma_parzyste / licznik_parzyste
else:
    srednia_parzyste = 0
    print('Brak cyfr parzystych')

if licznik_nieparzyste > 0:
    srednia_nieparzyste = suma_nieparzyste / licznik_nieparzyste
else:
    srednia_nieparzyste = 0
    print('Brak cyfr nieparzystych')

if srednia_parzyste > 0 and srednia_nieparzyste > 0:
    print(f'Stosunek średnich: {srednia_parzyste / srednia_nieparzyste}')
else:
    print('Nie można obliczyć stosunku średnich, jedna ze średnich wynosi 0')

#zad.9.
number = input('Podaj liczbę: ')
dzielniki = []

for i in range(1, int(number)+1):
    if int(number) % i == 0:
        dzielniki.append(i)
suma_dzielnikow = 0
for dzielnik in dzielniki:
    suma_dzielnikow += dzielnik
    print(dzielnik)
if suma_dzielnikow == number:
    print(f'{number} to liczba doskonała!')

#zad.10.
number = input('Podaj liczbę: ')
dzielniki = []

for i in range(1, int(number)+1):
    if int(number) % i == 0:
        dzielniki.append(i)


if len(dzielniki) >- 2 or number == 1 or number == 0:
    print(f'{number} nie jest liczbą pierwszą!')

else:
    print(f'{number} jest liczbą pierwszą!')



for i in range(1, int(number)):
    dzielniki1 = []
    for j in range(1, i+1):
        if i % j == 0:
            dzielniki1.append(j)
    if len(dzielniki1) == 2:
        print(i)

