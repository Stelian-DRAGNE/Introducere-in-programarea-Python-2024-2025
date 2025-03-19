
suma = 0

while True:
    valoare = input("Introduceti un numar:\n")
    if valoare.isnumeric():
        valoare = int(valoare)
        suma = suma + valoare
    elif not valoare:
        print("Suma este:", suma)
        suma = 0
    else:
        print("Valoare nenumerica.")

