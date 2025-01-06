class Samochod:
    def __init__(self, marka, zuzyciePaliwa):
        self.marka = marka
        self.zuzyciePaliwa = zuzyciePaliwa

    def koszt(self, km, cena):
        return self.zuzyciePaliwa * km * cena

    def wyswietl(self):
        print(f"Marka samochodu: {self.marka}\nZużycie paliwa: {self.zuzyciePaliwa} ")

class Autobus(Samochod):
    def __init__(self, marka, zuzyciePaliwa, lMiejsc):
        super().__init__(marka, zuzyciePaliwa)
        self.lMiejsc = lMiejsc

    def wyswietl(self):
        print(f"Marka samochodu: {self.marka}\nZużycie paliwa: {self.zuzyciePaliwa}\nLiczba miejsc: {self.lMiejsc} ")

class Ciezarowka(Samochod):
    def __init__(self, marka, zuzyciePaliwa, nosnosc):
        super().__init__(marka, zuzyciePaliwa)
        self.nosnosc = nosnosc

    def wyswietl(self):
        print(f"Marka samochodu: {self.marka}\nZużycie paliwa: {self.zuzyciePaliwa}\nNośność: {self.nosnosc} ")


samochod = Samochod("Toyota", 6.5)
autobus = Autobus("Mercedes", 20.0, 50)
ciezarowka = Ciezarowka("Volvo", 30.0, 10000)

samochod.wyswietl()
print(f"Koszt przejazdu 100 km przy cenie paliwa 6.5 zł: {samochod.koszt(100, 6.5)} zł")

autobus.wyswietl()
print(f"Koszt przejazdu 100 km przy cenie paliwa 6.5 zł: {autobus.koszt(100, 6.5)} zł")

ciezarowka.wyswietl()
print(f"Koszt przejazdu 100 km przy cenie paliwa 6.5 zł: {ciezarowka.koszt(100, 6.5)} zł")
