def analiza_czestosci(nazwaPliku):
    nazwaWy = "czestosc_" + nazwaPliku  
    slownik_czestosci = {}
    plikWe = open(nazwaPliku, 'r')
    for linia in plikWe:
        linia = linia.strip().lower()
        slowa = linia.split()
        for slowo in slowa:
            slowo = ''.join([znak for znak in slowo if znak.isalnum()])
            if slowo:
                if slowo in slownik_czestosci:
                    slownik_czestosci[slowo] += 1
                else:
                    slownik_czestosci[slowo] = 1
    plikWe.close()

    posortowane_slowa = sorted(slownik_czestosci.items(), key=lambda x: x[1], reverse=True)

    plikWy = open(nazwaWy, 'w')
    for slowo, liczba in posortowane_slowa:
        plikWy.write(f"{slowo}: {liczba}\n")
    plikWy.close()

    print(f"Wyniki zapisano w pliku: {nazwaWy}")

analiza_czestosci("testowy.txt")