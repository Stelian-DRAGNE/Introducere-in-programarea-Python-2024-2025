
dictionar = { "cal":"alb", "pepene":"rosu", "dodge":"negru" }
print(dictionar.items())

# Iterare
for i in dictionar:
    print(i, dictionar[i])

# Iterare prin chei valoare 
for i in dictionar.items():
    print(i)

for k, v in dictionar.items():
    print(k, v)
    
    
# Citire
print(dictionar["cal"])

# Inserare
dictionar["mugurel"] = "verde"
print(dictionar)

# Update
dictionar["dodge"] = "albastru"
print(dictionar)

# Nerecomandat de a avea Key numere
dictionar[5] = "cinci"      
print(dictionar)

dictionar[()] = "Hello !"      
print(dictionar)

# dictionar[[]] = "World !"      # Cheile trebuie sa fie elemente imutabile.
# print(dictionar)