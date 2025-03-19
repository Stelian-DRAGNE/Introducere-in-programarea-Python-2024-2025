# index 0, 1, 2, 3, 4
a   =  [1, 2, 3, 4, 5]
b   =  [4, 5, 6, 7, 8]


print(type(a), type(a[0]))

# Iteratie
# for i in a:
#     print("i = ", i)

# Iteratie
# for i in b:
#     print("i = ", i)

print("Iterez prin indecsi:")

c = []
print("c = ", c)
for i in range(len(a)):
    print("i = ", i)
    c.append(a[i] + b[i])
    print("c = ", c)
    
print(c)