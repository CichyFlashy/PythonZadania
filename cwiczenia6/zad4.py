def szyfruj(nazwaWe, przesun):
    nazwaWy = 'zaszyfrowane_' + nazwaWe

    with open(nazwaWe, 'r') as plikWe, open(nazwaWy, 'w') as plikWy:
        for linia in plikWe:
            zaszyfrowana_linia = ""
            for znak in linia:
                if znak.isalpha():
                    if znak.islower():
                        zaszyfrowana_linia += chr((ord(znak) - ord('a') + przesun) % 26 + ord('a'))
                    elif znak.isupper():
                        zaszyfrowana_linia += chr((ord(znak) - ord('A') + przesun) % 26 + ord('A'))
                else:
                    zaszyfrowana_linia += znak
            plikWy.write(zaszyfrowana_linia)


def deszyfruj(nazwaWe, przesun):
    nazwaWy = 'deszyfrowane_' + nazwaWe

    with open(nazwaWe, 'r') as plikWe, open(nazwaWy, 'w') as plikWy:
        for linia in plikWe:
            deszyfrowana_linia = ""
            for znak in linia:
                if znak.isalpha():
                    if znak.islower():
                        deszyfrowana_linia += chr((ord(znak) - ord('a') - przesun) % 26 + ord('a'))
                    elif znak.isupper():
                        deszyfrowana_linia += chr((ord(znak) - ord('A') - przesun) % 26 + ord('A'))
                else:
                    deszyfrowana_linia += znak
            plikWy.write(deszyfrowana_linia)


deszyfruj("testowy.txt_zaszyfrowane", 2)

