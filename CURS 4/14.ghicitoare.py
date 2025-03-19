import random

while True:
    utilizator = int(input("Introduceti o valoare\n"))
    calculator = random.randint(1, 10)

    if utilizator > 10 or utilizator < 1:
        continue
    elif utilizator == calculator:
        print("Ai ghicit")
    else:
        print("Nu ai ghicit")

    print("Calculator", calculator)