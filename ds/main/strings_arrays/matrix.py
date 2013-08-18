import random

numbers_range = (0, 99)


def construct_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append( [random.randint(numbers_range[0], numbers_range[1]) for j in range(size)] )
    return matrix


def print_matrix(matrix):
    for l in matrix:
        for item in l:
            print '{:3}'.format(item),
        print
    print


def set_matrix_row_col_zero(matrix, size):
    rows = []
    cols = []

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for r in rows:
        for c in range(size):
            matrix[r][c] = 0

    for c in cols:
        for r in range(size):
            matrix[r][c] = 0


def test():
    mat = construct_matrix(5)
    set_matrix_row_col_zero(mat)
    print_matrix(mat)


if __name__ == '__main__':
    size = 5
    m = construct_matrix(size)
    print_matrix(m)
    set_matrix_row_col_zero(m, size)
    print_matrix(m)
