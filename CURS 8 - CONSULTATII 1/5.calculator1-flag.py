
numere = []

is_running = True

while is_running:
    valoare = input("Introduceti un numar:\n")
    
    if valoare.isnumeric():
        valoare = int(valoare)
        numere.append(valoare)
        
    elif not valoare:
        print("Suma este:", sum(numere))
        numere = []
        
    elif valoare == "exit":
        is_running = False
    
    else:
        print("Valoare nenumerica.")