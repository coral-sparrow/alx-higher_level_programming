#!/usr/bin/python3

'''
    module for simple matrix division calculations.
'''


def matrix_divided(matrix, div):
    '''
        function to apply matrix division element wise by a number (int/float).
    '''

    # matrix must be list
    if not isinstance(matrix, list):
        raise TypeError(('matrix must be a matrix (list of lists) of'
                         ' integers/floats'))

    # matrix rows must be lists
    if not all([isinstance(row, list) for row in matrix]):
        raise TypeError(('matrix must be a matrix (list of lists) of'
                         ' integers/floats'))

    # matrix row elements must be of type [int, float]
    if not all([isinstance(element, (float, int)) for row in matrix
                for element in row]):
        raise TypeError(('matrix must be a matrix (list of lists) of'
                         ' integers/floats'))

    # all rows have the same size
    if len(set([len(row) for row in matrix])) != 1:
        raise TypeError(('Each row of the matrix must'
                         ' have the same size'))

    # only number devision is allowed
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # divide by zero is not allowed
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [row.copy() for row in matrix]
    for row in new_matrix:
        for i in range(len(row)):
            row[i] /= div

    return new_matrix
