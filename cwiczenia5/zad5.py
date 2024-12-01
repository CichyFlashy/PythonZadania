def strcut(text: str, start: int, length: int) -> str:
    result = ""
    for i in range(start, start + length):
        result += text[i]
    return result

print(strcut("Ala ma kota", 1, 2)) # Oczekiwany wynik: "la"
print(strcut("Ala ma kota", 5, 4)) # Oczekiwany wynik: "a ko"