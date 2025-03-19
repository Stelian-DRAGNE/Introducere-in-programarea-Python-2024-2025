
# Creati un program care va lua de la utilizator pretul produsului si va calcula pretul final, cu taza inclusa.
# In cadrul programului este hardcodata taxa la valoarea de 20%.

pret = input("Introdu valoarea fara TVA:\n")
print("Ai introdus:", pret)

# TRansfor stringul in intreg
pret = int(pret)

pret_cu_tva = pret * 1.2
print(pret_cu_tva)