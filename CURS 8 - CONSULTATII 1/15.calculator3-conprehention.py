
# Versiune clasica

lista_numere = []
for j in range(2):
    numere = []
    for i in range(3):
        numere.append(i)
    # print(numere)
    lista_numere.append(numere)
print(lista_numere)

# # Versiune List comprehention
numere = [[i for i in range(3)] for j in range(2)]
print(numere)

# # Rezultat asteptat : [[0, 1, 2], [0, 1, 2]]