
# print(not(True and False) or (not True and False))
# print(not False or (False and False))
# print(not False or False)
# print(True or False)

A = True
B = False
print(not(A or B) == (not A and not B))
print(not(True or False) == (not True and not False))
print(False == False)