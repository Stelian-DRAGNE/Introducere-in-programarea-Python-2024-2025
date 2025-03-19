
dictionar = { "cal":"alb", "pepene":"rosu", "dodge":"negru" }

print(dictionar["pepene"])

if "piersica" in dictionar:
    print(dictionar["piersica"])
else:
    print("Piersica nu exista.")

print(dictionar.get("piersica"))
print(dictionar.get("cal"))
print(dictionar.get("piersica", "NEREUSIT"))
print(dictionar.get("cal", "NEREUSIT"))