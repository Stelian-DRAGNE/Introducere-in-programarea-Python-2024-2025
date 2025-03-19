
numar = input("Introduceti un numar\n")

# while numar.isnumeric() == False:
while not numar.isnumeric():
    numar = input("Introduceti un numar\n")
numar = int(numar)

if numar % 2 == 0:
    print("Par")
else:
    print("Impar")
