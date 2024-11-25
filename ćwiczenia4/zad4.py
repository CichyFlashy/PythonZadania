alphabet = "abcdefghijklmnopqrstuvwxyz"
string = input("Podaj ciąg znaków do zakodowania: ")
jumps = int(input("Podaj liczbę przesunięć: "))

result = ""
for i in string:
    index = alphabet.index(i)
    index2 = (index + jumps) % 26
    result += alphabet[index2]

print(f"Zaszyfrowany tekst: {result}")
