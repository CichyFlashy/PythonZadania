def strpos(text: str, z: str) -> int:
    text = text.lower()
    z = z.lower() 
    for i in range(len(text)):
        if text[i] == z:
            return i
    return -1


print(strpos("Ala ma kota", "a"))  # Oczekiwany wynik: 1
print(strpos("Ala ma kota", "z"))  # Oczekiwany wynik: -1
       