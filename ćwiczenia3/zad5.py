def number_to_string(n):
    jednostki = {
        0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery",
        5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć"
    }
    dziesiatki = {
        10: "dziesięć", 11: "jedenaście", 12: "dwanaście",
        13: "trzynaście", 14: "czternaście", 15: "piętnaście",
        16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście", 19: "dziewiętnaście"
    }
    dziesiatki_okr = {
        2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści",
        5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt",
        8: "osiemdziesiąt", 9: "dziewięćdziesiąt"
    }
    setki = {
        1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta",
        5: "pięćset", 6: "sześćset", 7: "siedemset",
        8: "osiemset", 9: "dziewięćset"
    }
    tysiac = "tysiąc"

    def three_digits(liczba):
        wynik = []
        if liczba >= 100: wynik.append(setki[liczba // 100])
        liczba %= 100
        if 10 <= liczba <= 19:
            wynik.append(dziesiatki[liczba])
        else:
            if liczba >= 20: wynik.append(dziesiatki_okr[liczba // 10])
            if liczba % 10 > 0: wynik.append(jednostki[liczba % 10])
        return " ".join(wynik)

    if n == 0: return jednostki[0]

    tysiac = n // 1000
    reszta = n % 1000
    wynik = []

    if tysiac > 0:
        if tysiac == 1:
            wynik.append("tysiąc")
        else:
            wynik.append(three_digits(tysiac))
            wynik.append("tysiące" if 2 <= tysiac % 10 <= 4 and tysiac not in {12, 13, 14} else "tysięcy")

    if reszta > 0:
        wynik.append(three_digits(reszta))

    return " ".join(wynik)

print(number_to_string(12))
print(number_to_string(542))
print(number_to_string(1))