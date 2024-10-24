#zad1

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
#zad2
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


