
# Varianta 1
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = []

lungimea_listelor = len(lista_a )

for i in range(lungimea_listelor):
    print("i = ", i)
    valoarea_din_a = lista_a[i]
    valoarea_din_b = lista_b[i]
    
    rezultat = valoarea_din_a + valoarea_din_b
    
    lista_c.append(rezultat)
print(lista_c)


# Varianta 2 - cea scurta
lista_c = [lista_a[i] + lista_b[i] for i in range(lungimea_listelor)]
print(lista_c) 