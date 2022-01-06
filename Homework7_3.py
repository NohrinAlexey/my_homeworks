import os
import shutil

main_folder = 'templates'
dir_path = 'my_project'

if os.path.exists(dir_path):
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.html'):
                    name_dir = os.path.join(main_folder, os.path.basename(root))
                    if not os.path.exists(name_dir):
                        os.makedirs(name_dir)
                    shutil.copyfile(os.path.join(root, file), os.path.join(name_dir, file))
        print("Файлы с расширением '.html' скопированы из родительской дериктории в ", "'", main_folder, "'", sep='')
    else:
        print("Директория с именем ", "'", main_folder, "'", " уже существует")
else:
    print("Директория с именем ", "'", dir_path, "'", " не существует.")
