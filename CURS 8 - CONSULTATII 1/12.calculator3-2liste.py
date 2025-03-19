
lista_a = []
lista_b = []

for lista_generica in [lista_a, lista_b]:
    for i in range(3):
        valoare = input("Introduceti un numar:\n")

        while not valoare.isnumeric():
            print("Introduceti o valoare numerica.")
            valoare = input("Introduceti un numar:\n")

        valoare = int(valoare)
        lista_generica.append(valoare)

print("Lista a:", lista_a)
print("Lista b:", lista_b)
