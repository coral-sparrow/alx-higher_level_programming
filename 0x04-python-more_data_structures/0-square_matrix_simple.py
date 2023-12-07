#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    t = []
    for row in matrix:
        tmp = []
        for i in row:
            tmp.append(i**2)
        t.append(tmp)
    return t
