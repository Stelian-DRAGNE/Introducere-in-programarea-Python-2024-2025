
while True:
    numar = input("Introduceti un numar\n")
    if numar.isnumeric():
        numar = int(numar)
        if numar % 2 == 0:
            print("Par")
        else:
            print("Impar")
    else:
        print("Nu ati introdus un numer")