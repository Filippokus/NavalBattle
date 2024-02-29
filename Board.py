from Ship import *
from Player import *

matrix = [[" " for _ in range(6)] for _ in range(6)]


def out(dot):
    return (dot.x < 0 or dot.x > 5) or (dot.y < 0 or dot.y > 5)


class Board:
    def __init__(self, hid=None, live_ships=0):
        self.list_ships = []
        self.list_contour = []
        self.list_shots = []
        self.hid = hid
        self.live_ships = live_ships
        self.list_contour_points = []
        self.list_miss = []

    def print_board(self):
        list1 = [dot for ship in self.list_ships for dot in ship.dots()]
        print("  ", end="")
        for i in range(1, 7):
            print(f"{i}|", end="")
        print()
        for i in range(6):
            print(f"{i + 1}|", end="")
            for j in range(6):
                dt = Dot(i + 1, j + 1)
                if dt in list1 and dt not in self.list_shots and self.hid:
                    print(f"■|", end="")
                elif dt in self.list_contour and self.hid and dt not in self.list_miss:
                    print(f".|", end="")
                elif dt in self.list_shots:
                    print(f"X|", end="")
                elif dt in self.list_contour_points:
                    print(f".|", end="")
                elif dt in self.list_miss:
                    print(f"T|", end="")
                else:
                    print(f"{matrix[i][j]}|", end="")
            print()

    def add_ship(self, ship: Ship):
        ship_dots = ship.dots()
        for dot in ship_dots:
            if out(dot):
                raise InvalidShipException(f"Корабль за пределами поля: точка {dot}")
            elif self.is_ship(dot):
                raise InvalidShipException("Тут стоит корабль")
            elif self.is_contour(dot):
                raise InvalidShipException("Невозможно разместить корабль рядом с другим кораблем")

        self.list_ships.append(ship)
        self.live_ships += 1
        self.contour(ship)

    def contour(self, ship: Ship, c=None):
        ship_dots = ship.dots()
        for dt in ship_dots:
            x, y = dt.x, dt.y
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < 6 and 0 <= j < 6 and (Dot(i + 1, j + 1) not in ship_dots):
                        if c is not None and not self.hid:
                            self.list_contour_points.append(Dot(i + 1, j + 1))
                        elif Dot(i + 1, j + 1) not in self.list_contour:
                            self.list_contour.append(Dot(i + 1, j + 1))

    def is_ship(self, dot):
        return Dot(dot.x + 1, dot.y + 1) in [dot for ship in self.list_ships for dot in ship.dots()]

    def is_contour(self, dot):
        return Dot(dot.x + 1, dot.y + 1) in self.list_contour

    def shot(self, dot: Dot):
        if dot in self.list_shots or dot in self.list_miss:
            raise AlreadyTakenException("Эта клетка уже была атакована. Пожалуйста, выберите другую.")
        elif dot in self.list_contour_points:
            raise AlreadyTakenException("Здесь не может быть корабля")
        else:
            f = False
            for ship in self.list_ships:
                if dot in ship.dots():
                    f = True
                    self.list_shots.append(dot)
                    ship.n_lives -= 1
                    if ship.n_lives == 0:
                        self.contour(ship, c=1)
                        self.live_ships -= 1
                        self.list_ships.remove(ship)
                        print(f"Корабль потоплен")
                    return True
            if not f:
                self.list_miss.append(dot)
        return False
