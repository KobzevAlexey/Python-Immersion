import random


class Matrix:

    def __init__(self, rows: int = 2, columns: int = 2, matrix: list[list[int]] = None):
        if matrix is None:
            if rows > 1 and columns > 1:
                self.rows = rows
                self.columns = columns
                self.matrix = [[random.randint(0, 100) for _ in range(columns)] for _ in range(rows)]
            else:
                raise ValueError
        else:
            if Matrix._check_matrix(matrix):
                self.rows = len(matrix)
                self.columns = len(matrix[0])
                self.matrix = matrix
            else:
                raise ValueError

    def __eq__(self, other):
        if Matrix._same(self, other):
            return all([all([self.matrix[r][c] == other.matrix[r][c]
                             for c in range(self.columns)]) for r in range(self.rows)])
        else:
            raise ValueError

    def __add__(self, other):
        if Matrix._same(self, other):
            return Matrix(matrix=[[self.matrix[i][j] + other.matrix[i][j]
                                   for j in range(self.columns)] for i in range(self.rows)])
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            new_matrix = [[0] * other.columns for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.columns):
                    for k in range(other.columns):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(matrix=new_matrix)

        elif isinstance(other, int | float):
            return Matrix(matrix=[[self.matrix[r][c] * other for c in range(self.columns)] for r in range(self.rows)])

        else:
            raise ValueError

    def __str__(self):
        return '\n'.join(''.join([f'{x:^5}' for x in row]).rstrip() for row in self.matrix)

    @staticmethod
    def _same(matrix_1, matrix_2):
        return isinstance(matrix_2, Matrix) and matrix_1.rows == matrix_2.rows and matrix_1.columns == matrix_2.columns

    @staticmethod
    def _check_matrix(matrix: list[list[int]]) -> bool:
        return len(set(map(len, matrix))) == 1


c = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(c * d)