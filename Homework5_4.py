src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [biggest_num for i, biggest_num in zip(src, src[1:]) if biggest_num > i]

print(result)
