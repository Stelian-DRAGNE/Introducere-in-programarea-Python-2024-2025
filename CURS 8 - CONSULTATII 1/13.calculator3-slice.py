
numere = []

for i in range(6):
    valoare = input("Introduceti un numar:\n")

    while not valoare.isnumeric():
        print("Introduceti o valoare numerica.")
        valoare = input("Introduceti un numar:\n")

    valoare = int(valoare)
    numere.append(valoare)

print(numere)
print("Lista a:", numere[:3])
print("Lista b:", numere[3:])