class TriangleException(Exception):
    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message

    def __str__(self):
        return f'Triangle Error!\n{self.name}\n{self.message}'


class TriangleExistsError(TriangleException):
    def __init__(self, side: float | int, other_sides: list[int | float]):
        self.side = side
        self.other_sides = tuple(other_sides)
        super().__init__('Ошибка создания',
                         f'Треугольник не может быть создан, т.к. сторона {self.side} '
                         f'больше суммы двух других сторон {self.other_sides}')


class TriangleNegativeValueError(TriangleException):
    def __init__(self, side):
        super().__init__(f'Ошибка! Сторона треугольника не может иметь отрицательную длину {side}')


class TriangleValueError(TriangleException):
    def __init__(self, side):
        super().__init__(f'Ошибка! Сторона треугольника должна быть числом {side}')
