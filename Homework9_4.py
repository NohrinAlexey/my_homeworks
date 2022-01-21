class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула нелево'

    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость town car {self.name}  {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} больше чем разрешено этому типу машин'
        else:
            return f'Скорость {self.name} нормальная скорость для этого типа машин'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость  work car {self.name} {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} больше чем разрешено этому типу машин'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'


audi = SportCar(100, 'Красный', 'Audi', False)
oka = TownCar(30, 'Белая', 'Oka', False)
lada = WorkCar(70, 'Жёлтая', 'Lada', True)
ford = PoliceCar(110, 'Синий',  'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} двигается со скоростью {lada.show_speed()} км/ч')
print(f'{lada.name}  {lada.color}')
print(f'{audi.name} полицейский автомобиль? {audi.is_police}')
print(f'{lada.name}  не полицейский автомобиль? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
