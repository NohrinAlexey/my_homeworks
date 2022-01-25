from time import sleep
from itertools import cycle

class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for color, time in cycle(TrafficLight.__color.items()):
            print(f'Светофор переключается \n '
                  f'{color}')
            for i in range(time, 0, - 1):
                sleep(1)
                print(i, end=' | ')
            print()
TrafficLight = TrafficLight()
TrafficLight.running()
