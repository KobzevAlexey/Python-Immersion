class TreeLine:
    def __init__(self, a, b, c):
        """Инициализация класса"""
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        """Метод вывода на печать __str__"""
        return f'линяя "а": {self.a}, линяя "b": {self.b}, линяя "с": {self.c}'

    def __add__(self, other):
        """Метод сложения"""
        a, b, c = ((self.a + other.a), (self.b + other.b), (self.c + other.c))
        return TreeLine(a, b, c)

    def __sub__(self, other):
        """Метод вычитания"""
        a, b, c = ((self.a - other.a), (self.b - other.b), (self.c - other.c))
        return TreeLine(a, b, c)

    def __eq__(self, other):
        """Метод сравнения == и != """
        a, b, c = self.a, self.b, self.c
        d, e, f = other.a, other.b, other.c
        return sorted((a, b, c)) == sorted((d, e, f))

    def __lt__(self, other):
        """Метод сравнения < или > """
        _bool = (self.a + self.b + self.c) < (other.a + other.b + other.c)
        return _bool

    def __le__(self, other):
        """Метод сравнения <=,  >= """
        _bool = self.__lt__(other) or self.__eq__(other)
        return _bool

    def __repr__(self):
        """Метод вывода на печать __repr__"""
        return f'TreeLine({self.a}, {self.b}, {self.c})'


tree_line = TreeLine(2, 3, 8)
tree_line_2 = TreeLine(1, 2, 3)
print(tree_line - tree_line_2)
print(tree_line + tree_line_2)
tree_line_3 = TreeLine(1, 2, 3)
print(tree_line_2 == tree_line_3)
print(tree_line_2 != tree_line_3)


print('меньше, больше')
print(tree_line > tree_line_3)
print(tree_line_2 < tree_line)
print(tree_line >= tree_line_3)


list_line = [tree_line, tree_line_2, tree_line, tree_line_3]
print(sorted(list_line))