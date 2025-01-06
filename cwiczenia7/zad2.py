class ElementZamowienia:
    def __init__(self, nazwa, cena, liczbaSztuk):
        self.__nazwa = nazwa
        self.__cena = cena
        self.__liczbaSztuk = liczbaSztuk

    def __str__(self):
        return f"{self.__nazwa} {self.__cena} zł, {self.__liczbaSztuk} szt., łącznie {self.__liczbaSztuk*self.__cena} zł"

    def obliczKoszt(self):
        return self.__cena * self.__liczbaSztuk * self.obliczRabat()

    def obliczRabat(self):
        if self.__liczbaSztuk >= 5:
            return 0.9
        else:
            return 1


class Zamowienie:
    def __init__(self, maksRozmiar):
        self.__elementy = []
        self.__rozmiar = 0
        self.__maksRozmiar = maksRozmiar

    def dodaj(self, elZam):
        if self.__rozmiar <= self.__maksRozmiar:
            self.__elementy.append(elZam)
            self.__rozmiar += 1
            return True
        else:
            return False

    def obliczKoszt(self):
        return sum(el.obliczKoszt() for el in self.__elementy)

    def pisz(self):
        print("Zamówienie:")
        for el in self.__elementy:
            print(el)
        calkowity_koszt = self.obliczKoszt()
        print(f"Łączny koszt zamówienia: {calkowity_koszt:.2f} zł")


z = Zamowienie(10)
z.dodaj(ElementZamowienia("Chleb", 4.0, 2))
z.dodaj(ElementZamowienia("Mleko", 2.5, 1))
z.dodaj(ElementZamowienia("Cukier", 4.0, 5))
z.dodaj(ElementZamowienia("Puszka", 9.0, 1))
z.pisz()