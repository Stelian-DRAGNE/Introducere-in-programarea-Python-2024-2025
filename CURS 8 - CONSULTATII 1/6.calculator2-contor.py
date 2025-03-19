
numere = []

contor = 0

while contor < 6:
    valoare = input("Introduceti un numar:\n")

    if valoare.isnumeric():
        valoare = int(valoare)
        numere.append(valoare)
        contor += 1

    else:
        print("Valoare nenumerica.")

print("Suma este:", sum(numere))