def szukaj(nazwaPlikWe, nazwaPlikWy, slowo):
    with open(nazwaPlikWe, "r", encoding="utf-8") as plikWe:
        with open(nazwaPlikWy, "w", encoding="utf-8") as plikWy:
            for linia in plikWe:
                if slowo in linia:
                    plikWy.write(linia)

szukaj("testowy.txt", "wynik.txt", "egzamin")

