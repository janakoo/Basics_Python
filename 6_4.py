class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def info(self):
        return  self.name + ' ' + self.color + ' ' + str(self.is_police)

    def show_speed(self):
        return self.speed

    def go(self):
        return f'Машина {self.color} {self.name} едет'
    def stop(self):
        return f'Машина {self.color} {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.color} {self.name} повернула {direction}'

class WorkCar(Car):
   def show_speed(self):
        if self.speed > 40:
            print("ВНИМАНИЕ! Превышена максимальная скорость!")
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("ВНИМАНИЕ! Превышена максимальная скорость!")
        return self.speed

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass



AutoWork = WorkCar(50,'красная','Kia',False)
print("_____________")
print('AutoWork:', '\n', AutoWork.go())
print("Ваша скорость " + str(AutoWork.show_speed())+ " км/ч")
print(AutoWork.turn("налево"), '\n', AutoWork.stop())


AutoTown = TownCar(55,'желтая','Chevrolet',False)
print("_____________")
print('AutoTown:', '\n', AutoTown.go())
print("Ваша скорость " + str(AutoTown.show_speed())+ " км/ч")
print(AutoTown.turn("налево"), '\n', AutoTown.stop())

AutoPolice = PoliceCar(150,'черная','BMW',True)
print("_____________")
print('AutoPolice:', '\n', AutoPolice.go())
print("Ваша скорость " + str(AutoPolice.show_speed())+ " км/ч")
print(AutoPolice.turn("направо"), '\n', AutoPolice.stop())

AutoSport = SportCar(200,'синяя','Maserati',False)
print("_____________")
print('AutoSport:', '\n', AutoSport.go())
print("Ваша скорость " + str(AutoSport.show_speed())+ " км/ч")
print(AutoSport.turn("налево"), '\n', AutoSport.turn("направо"), '\n',AutoSport.stop())