
startDate = int(input("Introduceti anul de inceput:\n"))
stopDate = int(input("Introduceti anul de sfarsit:\n"))

# Verificare startDate < stopDate
print()

if startDate < stopDate:
    for i in range(startDate, stopDate + 1):
        print(i)
else:
    for i in range(startDate, stopDate -1, -1):
        print(i)