string = input("Podaj tekst: ")
suma = 0

for i in string:
    if i.isdigit():
        suma += int(i)

print(f"Suma cyfr w podanych tekście wynosi: {suma}")