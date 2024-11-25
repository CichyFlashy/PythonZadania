string = input("Podaj ciąg znaków: ")
last_char = string[-1]
counter = 0
for i in string:
    if i == last_char:
        counter += 1

print(f"Znak {last_char} pojawił się w ciągu znaków {counter} razy.")