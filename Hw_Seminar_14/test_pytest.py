import pytest
from matrix import Matrix


def test_matrix_multiplication():
    c = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    d = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    result = c * d
    expected_matrix = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

    assert result.matrix == expected_matrix


def test_matrix_addition():
    c = Matrix(matrix=[[1, 2], [3, 4]])
    d = Matrix(matrix=[[5, 6], [7, 8]])

    result = c + d
    expected_matrix = [[6, 8], [10, 12]]

    assert result.matrix == expected_matrix


def test_matrix_scalar_multiplication():
    c = Matrix(matrix=[[1, 2], [3, 4]])

    result = c * 2
    expected_matrix = [[2, 4], [6, 8]]

    assert result.matrix == expected_matrix


def test_matrix_equality():
    c = Matrix(matrix=[[1, 2], [3, 4]])
    d = Matrix(matrix=[[1, 2], [3, 4]])
    e = Matrix(matrix=[[5, 6], [7, 8]])

    assert c == d
    assert not c == e


def test_invalid_matrix_creation():
    with pytest.raises(ValueError):
        Matrix(rows=0, columns=2)

    with pytest.raises(ValueError):
        Matrix(matrix=[[1, 2], [3]])


if __name__ == '__main__':
    pytest.main()
