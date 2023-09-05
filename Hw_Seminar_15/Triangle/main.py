import sys
from exceptiom_triangle import TriangleExistsError, TriangleValueError, TriangleNegativeValueError


class Side:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.parameter_name, value)

    @staticmethod
    def validate(side):
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
                raise TriangleExistsError(side, other_sides)
        return True


def create_triangle_from_command_line_arguments():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 4:
        print("\nUsage: python script.py side_a side_b side_c\n")
        return

    # Extract the side lengths from command line arguments
    side_a, side_b, side_c = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the triangle
    try:
        triangle = Triangle(side_a, side_b, side_c)
        print(f"Triangle created successfully: {triangle}")
    except (TriangleExistsError, TriangleValueError, TriangleNegativeValueError) as e:
        print(f"Triangle creation failed: {e}")


if __name__ == "__main__":
    create_triangle_from_command_line_arguments()


# для вызова из консоли - python main.py 5 5 9
