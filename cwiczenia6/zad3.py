import os

def sumuj_i_zapisz(nazwaPliku) -> int:
    if not os.path.exists(nazwaPliku):
        plik = open(nazwaPliku, "w")
        plik.write("1\n")
        plik.close()
        return 1
    else:
        suma = 0
        plik = open(nazwaPliku, "r")
        for linia in plik:
            linia = linia.strip()
            if linia.isdigit():
                suma += int(linia)
        plik.close()
        plik = open(nazwaPliku, "a")
        plik.write(f"{suma + 1}\n")
        plik.close()
        return suma + 1


print(sumuj_i_zapisz("liczby.txt"))

