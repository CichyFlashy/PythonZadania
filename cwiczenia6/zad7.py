def analiza_sentymentu(nazwaPliku):
    pozytywnePlik = "pozytywne.txt"
    negatywnePlik = "negatywne.txt"

    plikPozytywne = open(pozytywnePlik, 'r')
    pozytywne_slowa = set()
    for linia in plikPozytywne:
        pozytywne_slowa.add(linia.strip().lower())
    plikPozytywne.close()

    plikNegatywne = open(negatywnePlik, 'r')
    negatywne_slowa = set()
    for linia in plikNegatywne:
        negatywne_slowa.add(linia.strip().lower())
    plikNegatywne.close()

    liczba_pozytywnych = 0
    liczba_negatywnych = 0
    liczba_neutralnych = 0

    plikWe = open(nazwaPliku, 'r')
    for linia in plikWe:
        linia = linia.strip().lower()
        slowa = linia.split()

        licznik_pozytywne = sum(1 for slowo in slowa if slowo in pozytywne_slowa)
        licznik_negatywne = sum(1 for slowo in slowa if slowo in negatywne_slowa)

        if licznik_pozytywne > licznik_negatywne:
            liczba_pozytywnych += 1
        elif licznik_negatywne > licznik_pozytywne:
            liczba_negatywnych += 1
        else:
            liczba_neutralnych += 1
    plikWe.close()

    nazwaWy = "wyniki_sentymentu.txt"
    plikWy = open(nazwaWy, 'w')
    plikWy.write(f"Liczba pozytywnych opinii: {liczba_pozytywnych}\n")
    plikWy.write(f"Liczba negatywnych opinii: {liczba_negatywnych}\n")
    plikWy.write(f"Liczba neutralnych opinii: {liczba_neutralnych}\n")
    plikWy.close()

analiza_sentymentu("opinie.txt")
