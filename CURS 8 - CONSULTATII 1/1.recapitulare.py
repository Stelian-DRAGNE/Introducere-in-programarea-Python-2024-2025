
# a = 12, 12, 14, 41
# print(a, type(a))


# a = 12, 3.2, 31
# print(a, type(a))


# a = 12_000_000
# print(a, type(a))
# print(f"{a:,}", type(a))
# print(f"{a:_}", type(a))


# x = 10
# y = 20
# x, y = y, x
# print("x =", x)
# print("y =", y)


# a, *b = 100, 200, 300, 400, 500
# print("a =", a)
# print("b =", b)

# *a, b = 100, 200, 300, 400, 500
# print("a =", a)
# print("b =", b)


# tuplu = (100, 100, 100)
# lista = [200, 300, 400]
# print("lista =", lista)
# lista.append(5)
# print("lista =", lista)
# lista.pop()
# print("lista =", lista)

# lista.insert(2, 6)
# print("lista =", lista)

# lista.pop(0)
# print("lista =", lista)

# print("tuplu =", tuplu)
# tuplu.append(5) - eroare - tuple este imutabil
# tuplu.insert(2, 6) - eroare - nu pot insera fiind ca este imutabil

# print("primul element lista =", lista[0])
# print("primul element tuplu =", tuplu[0])
# lista[0] = "modificat"
# print("primul element lista =", lista[0])
# print("lista =", lista)

# tuplu[0] = "modificat" - eroare - este imutabil


x, y, z = 0, 1, 0
if 1 in (x, y, z):
    print("Yes, it does.")
else:
    print("No chance.")