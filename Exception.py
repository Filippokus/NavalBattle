class BoardOutException(Exception):
    def __init__(self, message="Выстрел за пределы игрового поля"):
        self.message = message
        super().__init__(self.message)


class AlreadyTakenException(Exception):
    def __init__(self, message="В эту клетку уже стреляли"):
        self.message = message
        super().__init__(self.message)


class InvalidShipException(Exception):
    def __init__(self, message="Невозможно разместить корабль"):
        self.message = message
        super().__init__(self.message)


class InvalidCoordinateException(Exception):
    def __init__(self, message="Координаты должны быть в диапазоне от 1 до 6."):
        self.message = message
        super().__init__(self.message)
