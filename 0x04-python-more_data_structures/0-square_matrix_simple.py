#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = matrix[:]

    for x in range(len(matrix)):
        mat[x] = list(map(lambda x: x ** 2, matrix[x]))
    return(mat)
