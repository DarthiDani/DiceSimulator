import abc


class Kostka(abc.ABC):
    @abc.abstractmethod
    def rzuć(self):
        """Rzuca kostką i zwraca wynik."""
        pass

    @abc.abstractmethod
    def przerzuć(self):
        """Przerzuca kostkę, zmienia wynik na nowy."""
        pass

    @abc.abstractmethod
    def pobierz_wynik(self):
        """Zwraca wynik ostatniego rzutu."""
        pass

    @abc.abstractmethod
    def rzuć_x_raz(self, x):
        """Rzuca kostką x razy i zwraca listę wyników."""
        pass

    @abc.abstractmethod
    def rzuć_x_raz_i_zsumuj(self, x):
        """Rzuca kostką x razy i zwraca sumę wyników."""
        pass
