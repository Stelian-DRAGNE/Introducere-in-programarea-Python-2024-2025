
# cuvant = "radar"            # da
# cuvant = "motor"            # nu
# cuvant = "asa"              # da
cuvant = "aerisirea"        # da

# Versiunea 1 - hardcodata
if cuvant[0] == cuvant[-1] and cuvant[1] == cuvant[-2] and cuvant[2] == cuvant[-3]:
    print("Este palindrom")
else:
    print("Nu este palindrom")

