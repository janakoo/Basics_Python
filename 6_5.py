class Stationery:
   def __init__(self, title):
       self.title = title

   def draw(self):
       return f'Запуск отрисовки деталей: '

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки деталей:"{self.title}"'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки деталей:"{self.title}"'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки деталей:"{self.title}"'



pen = Pen('Запись в тетради делаем синей ручкой')
print(pen.draw())

pencil = Pencil('Ударение в словах ставим карандашом')
print(pencil.draw())

handle = Handle('Маркером выделяем ошибки и места требующие доработки')
print(handle.draw())