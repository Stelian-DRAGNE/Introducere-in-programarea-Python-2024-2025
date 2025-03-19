
numere = []

while len(numere) < 6:
    valoare = input("Introduceti un numar:\n")

    if valoare.isnumeric():
        valoare = int(valoare)
        numere.append(valoare)

    else:
        print("Valoare nenumerica.")

print("Suma este:", sum(numere))