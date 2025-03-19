
numere  = [32, 41, 51, 51, 12, 3, 1, 312, 8, 423]

# Introduceti un numer de la tastatura 
introdus = int(input("Introduceti un numer de la tastatura \n"))

# Spuneti daca este in lista numere
# Versiunea 1
for i in numere:
    if i == introdus:
        print("Se afla in lista")
        break
else: 
    print("Nu se afla in lista")


# Versiunea 2
se_afla = False
for i in numere:
    if i == introdus:
        se_afla = True
if se_afla:
    print("Se afla in lista")
else: 
    print("Nu se afla in lista")


# Versiunea 3
if introdus in numere:
    print("Se afla in lista")
else: 
    print("Nu se afla in lista")