
startDate = int(input("Introduceti anul de inceput:\n"))
stopDate = int(input("Introduceti anul de sfarsit:\n"))

print(f"Anii intre {startDate} si {stopDate}")
for i in range(startDate, stopDate + 1):
    print(i)