some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0
for i in range(len(some_list)):
    prefix = ""
    item_of_list = some_list[index]
    if "+" in item_of_list:
        prefix, item_of_list = item_of_list[0], item_of_list[1]
    if item_of_list.isdigit():
        num = int(item_of_list)
        some_list[index] = '{}{:02d}'.format(prefix, num)
        some_list.insert(index, '"')
        some_list.insert(index + 2, '"')
        index += 3
    else:
        index += 1

sting_from_some_list = " ".join(some_list)
print(sting_from_some_list)