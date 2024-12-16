import os

def sumuj_i_zapisz(nazwaPliku) -> int:
    if not os.path.exists(nazwaPliku):
        file = open(nazwaPliku, "w")
        file.write("1\n")
        file.close()
        return 1
    else:
        result = 0
        file = open(nazwaPliku, "r")
        for line in file:
            line = line.strip()
            if line.isdigit():
                result += int(line)
        file.close()
        file = open(nazwaPliku, "a")
        file.write(f"{result + 1}\n")
        file.close()
        return result + 1


print(sumuj_i_zapisz("liczby.txt"))

