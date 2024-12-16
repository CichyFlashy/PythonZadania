def analiza_uczniow(nazwaPliku):
    nazwaWy = "posortowani_uczniowie.txt"
    dane_uczniow = []
    plikWe = open(nazwaPliku, 'r')
    for linia in plikWe:
        linia = linia.strip()
        if linia:
            dane = linia.split()
            imie = dane[0]
            nazwisko = dane[1]
            oceny = [int(ocena) for ocena in dane[2:]]
            srednia = sum(oceny) / len(oceny)
            dane_uczniow.append((imie, nazwisko, srednia))
    plikWe.close()
    dane_uczniow.sort(key=lambda x: x[2], reverse=True)
    plikWy = open(nazwaWy, 'w')
    for imie, nazwisko, srednia in dane_uczniow:
        plikWy.write(f"{imie} {nazwisko} {srednia:.2f}\n")
    plikWy.close()

    print(f"Wyniki zapisano w pliku: {nazwaWy}")

analiza_uczniow("uczniowie.txt")