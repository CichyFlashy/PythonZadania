def szukaj(nazwaPlikWe, nazwaPlikWy, slowo):
    with open(nazwaPlikWe, "r", encoding="utf-8") as plikWe:
        with open(nazwaPlikWy, "w", encoding="utf-8") as plikWy:
            for line in plikWe:
                if slowo in line:
                    plikWy.write(line)

szukaj("testowy.txt", "wynik.txt", "egzamin")

