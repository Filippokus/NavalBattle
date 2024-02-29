from Board import *
from Player import *
from Exception import *
from Ship import *
import random


class Game:
    def __init__(self):
        self.board = Board(hid=True)
        self.ai_board = Board(hid=False)
        self.player = User(self.board, self.ai_board)
        self.ai = AiPlayer(self.ai_board, self.board)

    def random_board(self):
        ships = [(3, 1), (2, 2), (1, 4)]
        a = 0
        self.ai_board.live_ships = 0
        self.ai_board.list_contour = []
        self.ai_board.list_ships = []
        for ship_length, ship_count in ships:
            for i in range(ship_count):
                while True:
                    dot_nose = [random.randint(1, 6), random.randint(1, 6)]
                    direction = random.randint(0, 1)
                    ship = Ship(ship_length, dot_nose, direction)
                    if a > 10:
                        return False
                    try:
                        self.ai_board.add_ship(ship)

                        break
                    except InvalidShipException:
                        a += 1
                        continue
        return True

    def create_board(self):
        # Задаем длины кораблей и количество кораблей каждой длины
        ship_lengths = [3, 2, 2, 1, 1, 1, 1]

        for length in ship_lengths:
            while True:
                try:
                    try:
                        in_val = input(
                            f"Введите координаты и направление(0 - горизонталь, 1 - вертикаль)"
                            f" для корабля длины {length}: ").split()
                        x = int(in_val[0])
                        y = int(in_val[1])
                        direction = int(in_val[2])
                        if direction not in (0, 1):
                            raise InvalidShipException(
                                f"Неверное значение для направления (0 - горизонтальное, 1 - вертикальное)")

                        if not 1 <= x <= 6 or not 1 <= y <= 6:
                            raise InvalidShipException(f"Координаты должны быть от 1 до 6.")
                    except IndexError:
                        print("Введи значения!")
                    else:

                        ship = Ship(length, [x, y], direction)
                        self.board.add_ship(ship)
                        self.board.print_board()

                        break  # Если корабль успешно добавлен, выходим из цикла
                except InvalidShipException as e:
                    print(f"Ошибка при добавлении корабля: {e}")

    @staticmethod
    def greet():
        messages = [
            "Приветствую, игрок! Нажимай Enter для продолжения.",
            "Это игра Морской бой!",
            "Тебе предстоит сразиться с игроком-компьютером",
            "Перед тем как мы начнем игру, тебе необходимо разместить корабли:\n"
            "1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.",
            "Давай приступим к расстановке, через пробел введи в консоль данные о корабле: \n"
            "длину корабля, первую координату, вторую координату, горизонтальный/вертикальный"
        ]
        for message in messages:
            print(message)
            input()

    def loop(self):
        while True:
            if self.random_board():
                print("Поле противника создано")
                break
        self.create_board()

        current_player = self.player
        while True:
            self.ai_board.print_board()
            self.board.print_board()
            print("Ход игрока" if current_player == self.player else "Ход компьютера")

            if current_player.move():
                if current_player.enemy_board.live_ships == 0:
                    self.ai_board.print_board()
                    self.board.print_board()
                    print("Вы выиграли!" if current_player == self.player else "Компьютер выиграл!")
                    break
            else:
                current_player = self.ai if current_player == self.player else self.player

    def start(self):
        self.greet()
        self.loop()


game = Game()
game.start()
