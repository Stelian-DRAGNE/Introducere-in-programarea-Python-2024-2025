
lista_a = [1, 2, 3, 100, 200, 300]
lista_b = [4, 5, 6, 7, 5, 5, 5, 5]

lista_c = []

if len(lista_a) > len(lista_b):
    min_lungimilor = len(lista_b)
    lista_lunga = lista_a
else:
    min_lungimilor = len(lista_a)
    lista_lunga = lista_b


for i in range(min_lungimilor):
    lista_c.append(lista_a[i] + lista_b[i])

print(lista_c)

# for i in lista_a[3:]:
#     lista_c.append(i)

lista_c += lista_lunga[min_lungimilor:]

print(lista_c)  