
startDate = int(input("Introduceti anul de inceput:\n"))
stopDate = int(input("Introduceti anul de sfarsit:\n"))

# Versiunea 1
# for i in range(startDate, stopDate + 1):
#     if i %4 == 0:
#         print(i)


# Versiunea 2
# if startDate % 4 == 0:
#     for i in range(startDate, stopDate + 1, 4):
#         print(i)
# else: 
#     for i in range((startDate // 4 + 1 * 4), stopDate + 1, 4):
#         print(i)


# Versiunea 3
for i in range((startDate // 4 + 1 * (startDate % 4 != 0)) * 4, stopDate + 1, 4):
        print(i)