
startDate = 1111
stopDate = 2222

if startDate > stopDate:
    aux = stopDate
    stopDate = startDate
    startDate = aux

print("startDate = ", startDate)
print("stopDate = ", stopDate)

startDate, stopDate = stopDate, startDate
print("startDate = ", startDate)
print("stopDate = ", stopDate)