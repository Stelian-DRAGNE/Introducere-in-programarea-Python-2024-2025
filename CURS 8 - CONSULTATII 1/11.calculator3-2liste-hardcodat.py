
lista_a = []
lista_b = []

for i in range(3):
    valoare = input("Introduceti un numar:\n")

    while not  valoare.isnumeric():
        print("Introduceti o valoare numerica.")
        valoare = input("Introduceti un numar:\n")

    valoare = int(valoare)
    lista_a.append(valoare)

for i in range(3):
    valoare = input("Introduceti un numar:\n")

    while not  valoare.isnumeric():
        print("Introduceti o valoare numerica.")
        valoare = input("Introduceti un numar:\n")

    valoare = int(valoare)
    lista_b.append(valoare)

print("Lista a:", lista_a)
print("Lista b:", lista_b)
