def counter_of_chars(text:str):
    chars = {}

    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars

string = "To jest przykładowo napisany tekst do przetestowania działania tego programu"
print(counter_of_chars(string))