import logging

logging.basicConfig(level=logging.INFO, filename="triangle.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')
logger = logging.getLogger(__name__)


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
        self.log_error()

    def log_error(self):
        logger.error(f"TriangleExistsError: {self.message}")


class TriangleNegativeValueError(TriangleException):
    def __init__(self, side):
        super().__init__(f'Ошибка! Сторона треугольника не может иметь отрицательную длину {side}')
        self.log_error()

    def log_error(self):
        logger.error(f"TriangleNegativeValueError: {self.message}")


class TriangleValueError(TriangleException):
    def __init__(self, side):
        super().__init__(f'Ошибка! Сторона треугольника должна быть числом {side}')
        self.log_error()

    def log_error(self):
        logger.error(f"TriangleValueError: {self.message}")


class Side:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        try:
            validated_value = self.validate(value)
            setattr(instance, self.parameter_name, validated_value)
        except TriangleException as e:
            logger.error(f"Triangle side assignment error: {e}")
            raise e

    def validate(self, side):
        if isinstance(side, (int, float)) and side > 0 or isinstance(side, str) and side.replace('.', '', 1).isdigit():
            return float(side)

        if isinstance(side, (float, int)) and side <= 0:
            raise TriangleNegativeValueError(side)

        if isinstance(side, str) and side.startswith('-') and side.replace('-', '', 1).replace('.', '', 1).isdigit():
            raise TriangleNegativeValueError(side)

        raise TriangleValueError(side)


class Triangle:
    side_a = Side()
    side_b = Side()
    side_c = Side()

    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self.sides = (self.side_a, self.side_b, self.side_c)
        self._is_exist()

    @property
    def type(self):
        sides_set = set(self.sides)
        if len(sides_set) == 1:
            return 'Равносторонний'
        elif len(sides_set) == 2:
            return 'Равнобедренный'
        else:
            return 'Разносторонний'

    def __str__(self):
        return f'{self.type} треугольник {self.sides}'

    def _is_exist(self):
        sides = list(map(float, self.sides))
        for side in sides:
            other_sides = sides.copy()
            other_sides.remove(side)
            if side >= sum(other_sides):
                message = f'Треугольник не может быть создан, т.к. сторона {side} ' \
                          f'больше или равна сумме двух других сторон {other_sides}'
                raise TriangleExistsError(side, other_sides)


if __name__ == "__main__":
    # Test the Triangle class with logging
    logger.info("Creating Triangle object")
    try:
        triangle = Triangle(3, 4, 10)
        logger.info(f"Triangle created successfully: {triangle}")
    except (TriangleExistsError, TriangleValueError, TriangleNegativeValueError) as e:
        logger.error(f"Triangle creation failed: {e}")
