
# letters = ["l", "a", "v", "a", "g", "m", "a", "n", "a"]

# 1. De cate ori se gaseste "a" in lista

# contor = 0
# for ch in letters:
#     if ch == "a":
#         contor += 1
# print(contor)

# print(letters.count("a"))


# 2. Care este caracterul care se gaseste de cele mai multe ori

# Ma astept freq = { "l":1, "a":3, "v":1, "g":1, "m":1, "n":1 }


letters = ["l", "a", "v", "a", "g", "m", "a", "n", "a"]
freq = {
    
}

for ch in letters:
    freq[ch] = 0
    
for ch in letters:
    freq[ch] += 1
print(freq)