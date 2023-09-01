import unittest
from matrix import Matrix


class MatrixTestCase(unittest.TestCase):

    def test_matrix_multiplication(self):
        c = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        d = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        result = c * d
        expected_matrix = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

        self.assertEqual(result.matrix, expected_matrix)

    def test_matrix_addition(self):
        c = Matrix(matrix=[[1, 2], [3, 4]])
        d = Matrix(matrix=[[5, 6], [7, 8]])

        result = c + d
        expected_matrix = [[6, 8], [10, 12]]

        self.assertEqual(result.matrix, expected_matrix)

    def test_matrix_scalar_multiplication(self):
        c = Matrix(matrix=[[1, 2], [3, 4]])

        result = c * 2
        expected_matrix = [[2, 4], [6, 8]]

        self.assertEqual(result.matrix, expected_matrix)

    def test_matrix_equality(self):
        c = Matrix(matrix=[[1, 2], [3, 4]])
        d = Matrix(matrix=[[1, 2], [3, 4]])
        e = Matrix(matrix=[[5, 6], [7, 8]])

        self.assertTrue(c == d)
        self.assertFalse(c == e)

    def test_invalid_matrix_creation(self):
        with self.assertRaises(ValueError):
            Matrix(rows=0, columns=2)

        with self.assertRaises(ValueError):
            Matrix(matrix=[[1, 2], [3]])


if __name__ == '__main__':
    unittest.main()
