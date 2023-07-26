# Напишите функцию для транспонирования матрицы


my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_matrix)):
    for j in range(len(my_matrix[i])):
        print(my_matrix[i][j], end='')
    print()


def transposing(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix


print()
my_matrix = transposing(my_matrix)

for i in range(len(my_matrix)):
    for j in range(len(my_matrix[i])):
        print(my_matrix[i][j], end='')
    print()
