def tabela_do_html(nazwaPliku):
    nazwaWy = "tabela.html"
    plikWe = open(nazwaPliku, 'r')
    wiersze = []
    for linia in plikWe:
        linia = linia.strip()
        if linia:
            wiersze.append(linia.split())
    plikWe.close()
    plikWy = open(nazwaWy, 'w')
    plikWy.write("<html><body>\n")
    plikWy.write("<table>\n")
    for wiersz in wiersze:
        plikWy.write("<tr>")
        for komorka in wiersz:
            plikWy.write(f"<td>{komorka}</td>")
        plikWy.write("</tr>\n")
    plikWy.write("</table>\n")
    plikWy.write("</body></html>")
    plikWy.close()
    print(f"Dane zostały zapisane do pliku: {nazwaWy}")

tabela_do_html("dane.txt")
