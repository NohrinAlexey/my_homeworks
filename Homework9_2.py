asphalt_thickness = 5
weight_of_asphalt = 5
road_width = 20
road_length = 5000


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def volume_asphalt(self):
        return (self._length * self._width * (weight_of_asphalt * asphalt_thickness) * asphalt_thickness) / 1000


a = Road(road_width, road_length)
print("На полотно площадь ", a._length * a._width, " м.кв. требуется ", a.volume_asphalt(), " т. асфальта", sep='')
