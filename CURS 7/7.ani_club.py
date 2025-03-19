
## feminim intre 16 si 70
## masculin intre 18 si 70

varsta = int(input("Introduceti varsta\n"))
gen = input("Introduceti genul (M / F)\n")

# Versiunea 1
if varsta < 16 or varsta > 70:
    print("Acces interzis")
elif varsta < 18 and gen == "M":
    print("Acces interzis")
else:
    print("Bine ati venit !")

# Versiunea 2
if varsta > 18 and varsta < 70:
    print("Bine ati venit !")
elif varsta > 16 and gen == "F":
    print("Bine ati venit !")
else:
    print("Acces interzis")

# Versiunea 3
if 18 < varsta < 70:
    print("Bine ati venit !")
elif varsta > 16 and gen == "F":
    print("Bine ati venit !")
else:
    print("Acces interzis")