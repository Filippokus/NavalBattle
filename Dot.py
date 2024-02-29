
class Dot:
    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1

    # def __hash__(self):
    #     return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x, self.y}'

    # def __repr__(self):
    #     return f'Dot({self.x}, {self.y})'
