
# suma = int(input("Introduceti suma:"))

suma = 128
print("Suma initiala :", suma)

bancnote_10 = suma // 10
print("Bancnote de 10 :", bancnote_10)

rest_dupa_10 = suma % 10
print("Rest :", rest_dupa_10)

bancnote_5 = rest_dupa_10 // 5
print("Bancnote de 5 :", bancnote_5)

rest_dupa_5 = rest_dupa_10 % 5
print("Rest :", rest_dupa_5)

bancnote_2 = rest_dupa_5 // 2
print("Bancnote de 2 :", bancnote_2)

rest_dupa_2 = rest_dupa_5 % 2
print("Rest :", rest_dupa_2)

bancnote_1 = rest_dupa_2 // 1
print("Bancnote de 2 :", bancnote_1)

rest_dupa_1 = rest_dupa_2 % 1
print("Rest :", rest_dupa_1)