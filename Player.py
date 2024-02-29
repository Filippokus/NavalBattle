import random

from Exception import *
from Dot import *


class Player:
    def __init__(self, board, enemy_board):
        self.board = board
        self.enemy_board = enemy_board

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                return self.enemy_board.shot(self.ask())
            except AlreadyTakenException:
                print("В эту клетку уже стреляли")
                continue


class User(Player):

    def ask(self):
        while True:
            try:
                x = int(input("Введите x: "))
                y = int(input("Введите y: "))
                if 0 < x < 7 and 0 < y < 7:
                    return Dot(x, y)
                else:
                    print("Координаты должны быть от 1 до 6. Попробуйте еще раз.")
            except ValueError:
                print("Вы указали неверный формат ввода. Попробуйте еще раз.")


class AiPlayer(Player):

    def __init__(self, board, ai_board):
        super().__init__(board, ai_board)
        self.used_dots = set()
        self.last_shot = None

    def ask(self):
        while True:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            if (x, y) not in self.used_dots:
                return Dot(x, y)

    def move(self):
        while True:
            try:
                return self.enemy_board.shot(self.ask())
            except AlreadyTakenException:
                continue
