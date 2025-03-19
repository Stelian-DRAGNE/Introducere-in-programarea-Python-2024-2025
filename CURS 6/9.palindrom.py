
# cuvant = "aerisirea"
cuvant = "racecar"
# cuvant = "elefaccafele"

inceput = 0
sfarsit = -1

for ch in cuvant:
    print(ch)
    ch_sfarsit = cuvant[sfarsit]
    if ch != cuvant[sfarsit]:
        print("Nu este palindrom")
        break
    sfarsit = sfarsit - 1
else:
    print("Este palindrom")