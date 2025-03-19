
## feminim intre 16 si 70
## masculin intre 18 si 70

varsta = int(input("Introduceti varsta\n"))
gen = input("Introduceti genul (M / F)\n")

## Versiunea 1 - range
if varsta in range(18, 71) and gen == "M":
    print("Bine ati venit !")
elif varsta in range(16, 71) and gen == "F":
    print("Bine ati venit !")
else:
    print("Acces interzis")

## Versiunea 2 - range
if (varsta in range(18, 71) and gen == "M") or (varsta in range(16, 71) and gen == "F"):
    print("Bine ati venit !")
else:
    print("Acces interzis")

# 18 - 2 * False
## Versiunea 3 - range
if (varsta in range(18 - 2 * (gen == "F"), 71)):
    print("Bine ati venit !")
else:
    print("Acces interzis")