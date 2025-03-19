
numere = []

while True:
    valoare = input("Introduceti un numar:\n")

    if valoare.isnumeric():
        valoare = int(valoare)
        numere.append(valoare)

    elif not valoare:
        print("Suma este:", sum(numere))
        numere = []

    elif valoare == "exit":
        break

    else:
        print("Valoare nenumerica.")