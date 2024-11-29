def html_to_rgb(color):
    hexadecimal = {'0':0, '1':1, '2':2, '3':3, '4':4,
                   '5':5, '6':6, '7':7, '8':8, '9':9,
                   'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    rgb_values = []
    for i in range(1, len(color), 2):
        hex_pair = color[i:i + 2].upper()  # Get the two characters for each color and convert to uppercase
        decimal = (16 * hexadecimal[hex_pair[0]]) + hexadecimal[hex_pair[1]]
        rgb_values.append(decimal)

    return rgb_values


print(html_to_rgb("#FF00AA"))
