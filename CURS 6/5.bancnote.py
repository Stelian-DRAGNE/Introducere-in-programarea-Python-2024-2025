"""

Recreati exercitiul anterior, astfel incat calculul sa se poata face pentru orice fel de grup de bancnote:
ex: 100, 50, 20, 10, 5
ex: 50, 10, 5, 1

"""

bancnote = [100, 50, 20, 10, 5, 1]
# bancnote = [10, 5, 2, 1]

print(type(bancnote))
suma_initiala = int(input("Introduceti suma\n"))
suma = suma_initiala

for valoare in bancnote:
    # print(valoare)
    nr_bancnote = suma // valoare
    print(f"Valoarea {valoare} ai {nr_bancnote} bancnote")
    
    suma = suma % valoare

print(suma_initiala)
print(suma_initiala)