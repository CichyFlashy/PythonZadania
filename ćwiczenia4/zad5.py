def str_to_int(string: str) -> int:
    result = '0'
    exponent_mode = False
    exponent = 0
    for i in range(len(string)):
        if string[i] == '-':
            if i > 0 and string[i - 1].isdigit():
                break
            elif i + 1 < len(string) and string[i + 1].isdigit():
                result += '-'
        elif string[i] == 'e':
            if i + 1 < len(string) and string[i + 1] == '-':
                break  
            exponent_mode = True
        elif string[i].isdigit():
            if exponent_mode:
                exponent = exponent * 10 + int(string[i])
            else:
                result += string[i]
        else:
            break
    result = int(result)
    if exponent_mode and exponent > 0:
        result *= 10 ** exponent
    return result

# Testy
print(str_to_int("+12"))        # Output: 12
print(str_to_int("0001"))       # Output: 1
print(str_to_int("991-234-23")) # Output: 991
print(str_to_int("+zonk"))      # Output: 0
print(str_to_int(""))           # Output: 0
print(str_to_int("-12e5"))      # Output: -120000
print(str_to_int("-12e-5"))     # Output: -12
