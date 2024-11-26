import random
from Kostka import Kostka


class Kostka20(Kostka):
    def __init__(self):
        self.wynik = None

    def rzuć(self):
        self.wynik = random.randint(1, 20)
        return self.wynik

    def przerzuć(self):
        if self.wynik is not None:
            self.wynik = random.randint(1, 20)
        else:
            raise ValueError("Nie rzucono jeszcze kostką!")
        return self.wynik

    def pobierz_wynik(self):
        if self.wynik is not None:
            return self.wynik
        else:
            raise ValueError("Nie rzucono jeszcze kostką!")

    def rzuć_x_raz(self, x):
        wyniki = [random.randint(1, 20) for _ in range(x)]
        return wyniki

    def rzuć_x_raz_i_zsumuj(self, x):
        wyniki = [random.randint(1, 20) for _ in range(x)]
        return sum(wyniki)
