
euro = 4.98
dolar = 4.71

suma_in_ron = input("Introduceti valoarea in lei\n")
suma_in_ron = int(suma_in_ron)
print("Aveti:", suma_in_ron, "RON")

suma_euro = suma_in_ron / euro
print("Aveti in EURO", suma_euro)
print("Aveti in EURO", round(suma_euro, 2))
print("Aveti in EURO", round(suma_euro, 4))

suma_dolar = suma_in_ron / dolar
print("Aveti in USD", suma_dolar)
print("Aveti in USD", round(suma_dolar, 2))
print("Aveti in USD", round(suma_dolar, 4))