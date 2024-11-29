string = input("Wpisz ciąg znaków: ")
string_len = len(string)


for i in range(1, int(string_len/2)):
    if string[i-1] != string[-i]:
        print("Ten ciąg nie jest palindromem.")
        break
else:
    print("Ten ciąg jest palindromem.")
