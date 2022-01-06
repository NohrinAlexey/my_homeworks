import os
new_project_name = input('Введите название для нового проекта: ')


root_folder = new_project_name
list_of_folders = ('settings', 'mainapp', 'adminapp', 'authapp')

if not os.path.exists(root_folder):
    os.mkdir(root_folder)
    os.chdir(root_folder)
    for folders in list_of_folders:
        dir_path = os.path.join(folders)
        if not os.path.exists(dir_path):    
            os.makedirs(dir_path)
else:
    print(f'Директория {root_folder} уже существует')