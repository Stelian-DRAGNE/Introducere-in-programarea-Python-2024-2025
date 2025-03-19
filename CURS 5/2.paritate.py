
numar = input("Introduceti un numar\n")
numar = int(numar)

# Versiunea 1
if numar % 2 == 0:
    print("Par")
else:
    print("Impar")

# Versiunea 2
print("Par") if numar % 2 == 0 else print("Impar")

# Versiunea 3
print("Impar") if numar % 2 != 0 else print("Par")
print("Impar") if numar % 2 == 1 else print("Par")

print("Impar") if numar % 2 else print("Par")

# Versiunea 4
print("Numarul este par", numar % 2 == 0)