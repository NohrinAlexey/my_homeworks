workers_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in workers_list:
    worker_name = employee.split()[-1].capitalize()
    print(f'Привет, {worker_name}!')