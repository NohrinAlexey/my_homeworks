def thesaurus(*names):
    result = {}
    for name in names:
        key = name[0]
        if name[0] not in result:
            result[key] = []
        result[key].append(name)
    return result

print(thesaurus("Иван", "Мария", "Петр", "Илья"))