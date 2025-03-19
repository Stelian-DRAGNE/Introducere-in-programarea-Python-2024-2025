
# Dupa modelul exercitiului anterior, calculati pretul cu TVA al apartamentelor:
    # - Daca pretul este mai mic de 140 000, TVA-ul este 5%
    # - Daca pretul este mai mare de 140 000, TVA-ul este 20%


pret = int(input("Introduceti pretul:\n"))

prag = 140_000

if pret < prag:
    print("Pretul este mai mic")
    pret_cu_tva = pret * 1.05
elif pret == prag:
    print("Pretul este egal")
    pret_cu_tva = pret * 1.20
else:
    print("Pretul este mai mare")
    pret_cu_tva = pret * 1.20

print("Pret cu TVA calculat este:", pret_cu_tva)