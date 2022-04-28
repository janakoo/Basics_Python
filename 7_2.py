from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param


    @property
    def m_square_coat(self):
       pass

    @property
    def m_square_suit(self):
        pass
    @abstractmethod
    def abstract(self):
        return 'заказ выполнен'

class Coat(Clothes):
    def m_square_coat(self):
        return round((self.param / 6.5 + 0.5), 2)
    def abstract(self):
        return 'заказ выполнен'
class Suit(Clothes):
    def m_square_suit(self):
      return round((self.param * 2 + 0.3), 2)
    def abstract(self):
        return 'заказ выполнен'
class Cloth:
    def cloth(self):
        return (coat.m_square_coat() + suit.m_square_suit())

    def abstract(self):
        return 'заказ выполнен'



coat = Coat(10)
print('метраж ткани на пальто:', coat.m_square_coat())
suit = Suit(2)
print('метраж ткани на костюм:', suit.m_square_suit())
cloth = Cloth()
print('общий метраж затраченной ткани:', cloth.cloth())
print(cloth.abstract())