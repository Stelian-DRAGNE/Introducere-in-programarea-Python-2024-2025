
## Introducem varsta
## Daca introduce ceva gresit (non-int), trebuie sa mai introduca o data / de mai multe ori

varsta = input("Introduceti varsta\n")
while not varsta.isnumeric:
    varsta = input("Introduceti o valoare intreaga\n")

varsta = int(varsta)


## Introducem genul doar daca nu este clar daca are acces sau nu
if varsta in range(18, 71):
    print("Bine ati venit !")
elif varsta < 16 or varsta > 70:
    print("Acces interzis")
else:
    gen = ("Introduceti genul\n")
    # while gen != "F" and gen != "M":
    while gen not in ["M", "F"]:
        gen = input("Alegeti intre M/F\n")
    if gen == "F":
        print("Bine ati venit !")
    else:
        print("Acces interzis")