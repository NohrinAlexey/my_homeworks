summa = 0
result1 = []
result2 = []
list_cube = [i ** 3 for i in range(1, 1001, 2)]
for value in list_cube:
    i = str(value)
    for digit in i:
        summa += int(digit)
    if summa % 7 == 0:
        result1.append(int(i))
    summa = 0
    j = str(value + 17)
    for digit in j:
        summa += int(digit)
    if summa % 7 == 0:
        result2.append(int(j))
    summa = 0

print(sum(result1), "Общая сумма")
print(sum(result2), "Общая сумма +17")
