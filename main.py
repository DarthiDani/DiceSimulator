from Kostka6 import Kostka6
from Kostka20 import Kostka20


def main():
    print("Witaj w programie Kostka!")
    print("1. Kostka sześcienna (1-6)")
    print("2. Kostka dwudziestościenna (1-20)")

    try:
        rodzaj_kostki = int(input("Wybierz rodzaj kostki (1 lub 2): "))
        if rodzaj_kostki == 1:
            kostka = Kostka6()
        elif rodzaj_kostki == 2:
            kostka = Kostka20()
        else:
            print("Nieprawidłowy wybór.")
            return

        while True:
            print("\nDostępne operacje:")
            print("1. Rzut kostką")
            print("2. Przerzut kostką")
            print("3. Pobierz wynik ostatniego rzutu")
            print("4. Rzuć wielokrotnie")
            print("5. Rzuć wielokrotnie i zsumuj wyniki")
            print("6. Wyjdź z programu")

            opcja = int(input("Wybierz operację (1-6): "))

            if opcja == 1:
                print("Wynik rzutu:", kostka.rzuć())
            elif opcja == 2:
                try:
                    print("Wynik przerzutu:", kostka.przerzuć())
                except ValueError as e:
                    print("Błąd:", e)
            elif opcja == 3:
                try:
                    print("Ostatni wynik:", kostka.pobierz_wynik())
                except ValueError as e:
                    print("Błąd:", e)
            elif opcja == 4:
                ile_razy = int(input("Ile razy chcesz rzucić? "))
                print("Wyniki:", kostka.rzuć_x_raz(ile_razy))
            elif opcja == 5:
                ile_razy = int(input("Ile razy chcesz rzucić? "))
                print("Suma wyników:", kostka.rzuć_x_raz_i_zsumuj(ile_razy))
            elif opcja == 6:
                print("Do widzenia!")
                break
            else:
                print("Nieprawidłowa opcja.")
    except ValueError:
        print("Błąd: Wprowadź liczbę.")


if __name__ == "__main__":
    main()
