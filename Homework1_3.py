idx = 0
for i in range(1, 101):
    idx += 1
    if 20 > i > 10:
        print(i, 'процентов')
    else:
        if idx == 1:
            print(i, 'процент')
        elif idx >= 5:
            print(i, 'процентов')
        elif 5 > idx > 1:
            print(i, 'процента')
        if idx == 10:
            idx = 0
