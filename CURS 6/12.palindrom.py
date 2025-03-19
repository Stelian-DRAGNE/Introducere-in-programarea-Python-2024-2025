
# cuvant = "radar"
# print("Lungimea:", len(cuvant))

# for i in range(len(cuvant)):
#     print("i =", i, "ch =", cuvant[i])
#     if cuvant[i] != cuvant[-1-i]:
#         print("Nu este palindrom.")
#         break
# else:
#     print("Cuvantul este palindrom.")


# cuvant = "aerisirea"
# print("Lungimea:", len(cuvant))

# for i in range(len(cuvant)):
#     print("i =", i, "ch =", cuvant[i])
#     if cuvant[i] != cuvant[-1-i]:
#         print("Nu este palindrom.")
#         break
# else:
#     print("Cuvantul este palindrom.")


cuvant = "aerisirea"
# cuvant = "asa"              # 1
# cuvant = "abba"             # 2
# cuvant = "radar"            # 2

print("Lungimea:", len(cuvant))

for i in range(len(cuvant) // 2):
    print("i =", i, "ch =", cuvant[i])
    if cuvant[i] != cuvant[-1-i]:
        print("Nu este palindrom.")
        break
else:
    print("Cuvantul este palindrom.")



"roma", "amor", "maro"