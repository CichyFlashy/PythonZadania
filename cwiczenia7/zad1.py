import math

class Wektor:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def dlugosc(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def normalizuj(self):
        dlugosc = self.dlugosc()
        return Wektor(self.__x / dlugosc, self.__y / dlugosc)

    def wyswietl(self):
        print(f"Wektor [{self.__x}, {self.__y}] o długości {self.dlugosc()}")

    def __add__(self, w):
        return Wektor(self.__x + w.__x, self.__y + w.__y)

    def __sub__(self, w):
        return Wektor(self.__x - w.__x, self.__y - w.__y)

    def __iadd__(self, w):
        self.__x += w.__x
        self.__y += w.__y
        return self

    def __isub__(self, w):
        self.__x -= w.__x
        self.__y -= w.__y
        return self

    def __str__(self):
        return f"[{self.__x}, {self.__y}]"

    def __mul__(self, a):
        return Wektor(self.__x * a, self.__y * a)

    def __rmul__(self, a):
        return Wektor(self.__x * a, self.__y * a)


w1 = Wektor(2, 4)
w2 = Wektor(1.5)
print("Wektor w1:", w1, "wektor w2:", w2)
print("Dł. w1 =", w1.dlugosc(), "dł. w2 =", w2.dlugosc())
print("w1+w2 =", w1+w2)
print("w1-w2 =", w1-w2)
print("w1*2 =", w1*2)
print("-3*w2 =", -3*w2)
print("w1*2-w2 =", w1*2-w2)
print("w1 po normalizacji =", w1.normalizuj())
print("w2 po normalizacji =", w2.normalizuj())
w1.wyswietl()
w2.wyswietl()
