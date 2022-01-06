import os


def file_size_stats():
    size_stats = {}

    for item in os.scandir('some_data'):
        if item.is_file():
            size = item.stat().st_size
            treshold = 10 ** len(str(size))
            ext = item.name.split('.')[-1]
            try:
                size_stats[treshold][0] += 1
                ext_list = size_stats[treshold][1]
                if ext in ext_list:
                    pass
                else:
                    ext_list.append(ext)
            except (KeyError, IndexError):
                size_stats[treshold] = [1, [ext]]
    print(sorted(size_stats.items()))
    print(size_stats)

if __name__ == '__main__':
    file_size_stats()
