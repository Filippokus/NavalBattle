from Dot import *


class Ship:
    def __init__(self, length: int, dot_nose: list, direction):
        self.length = length
        self.dot_nose = dot_nose
        self.n_lives = length
        self.direction = direction
        # self.contour = []

    def dots(self):
        list_dots = []
        x, y = self.dot_nose
        for i in range(self.length):
            if self.direction == 0:
                list_dots.append(Dot(x, y + i))
            if self.direction == 1:
                list_dots.append(Dot(x + i, y))
        return list_dots
