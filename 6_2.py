class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        print(f'Для покрытия всего дорожного полотна неободимо {self._length * self._width * self.weight * self.height / 1000} тонн асфальта')


r = Road(5000, 20)
r.asphalt_mass()