def emerytura(nazwaPliku):

    wiek_emerytalny_k = 60  
    wiek_emerytalny_m = 65 

    plik = open(nazwaPliku, 'r')
    linie = plik.readlines()
    plik.close()

    plik_kobiety = open("kobiety.txt", "w")
    plik_mezczyzni = open("mezczyzni.txt", "w")

    for linia in linie:
        dane = linia.strip().split()
        if len(dane) == 4:  
            imie, nazwisko, plec, wiek = dane
            if wiek.isdigit():
                wiek = int(wiek)
                lata_do_emerytury = 0

                if plec == 'K':
                    lata_do_emerytury = max(0, wiek_emerytalny_k - wiek)
                    plik_kobiety.write(f"{nazwisko} {imie} {lata_do_emerytury}\n")
                elif plec == 'M':
                    lata_do_emerytury = max(0, wiek_emerytalny_m - wiek)
                    plik_mezczyzni.write(f"{nazwisko} {imie} {lata_do_emerytury}\n")

    plik_kobiety.close()
    plik_mezczyzni.close()


emerytura("pracownicy.txt")
