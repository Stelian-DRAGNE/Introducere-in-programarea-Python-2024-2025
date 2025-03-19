
pret = int(input("Introduceti pretul:\n"))

prag = 140_000

pret_cu_tva = (pret * 1.05 if pret < prag else pret * 1.20)
print("Pret cu TVA calculat este:", pret_cu_tva)


procent = 1.05 if pret < prag else 1.20
print("Pret cu TVA calculat este:", pret * procent)