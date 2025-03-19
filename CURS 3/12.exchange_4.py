
euro = 4.98
dolar = 4.71
pounds = 5.99

suma_in_ron = input("Introduceti valoarea in lei\n")
suma_in_ron = int(suma_in_ron)
print("Aveti:", suma_in_ron, "RON")

while True:
    moneda = input("Introduceti moneda (euro/usd)\n")

    if moneda == "euro":
        suma_euro = suma_in_ron / euro
        print("Aveti in EURO", round(suma_euro, 2))
        break
    elif moneda == "usd":
        suma_dolar = suma_in_ron / dolar
        print("Aveti in USD", round(suma_dolar, 2))
        break
    elif moneda == "pounds":
        suma_pounds = suma_in_ron / pounds
        print("Aveti in GBP", round(suma_pounds, 2))
        break
    else:
        print("Nu stim moneda")