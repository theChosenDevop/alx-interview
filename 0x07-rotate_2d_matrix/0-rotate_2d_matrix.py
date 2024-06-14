#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate matrix 90 degrees clockwise
       Args:
            matrix [List]: List of integers
    """
    matrix_len = len(matrix)

    for row in range(matrix_len):
        for col in range(row + 1, matrix_len):
            matrix[col][row], matrix[row][col] = matrix[row][col], \
                    matrix[col][row]

    for i in range(matrix_len):
        matrix[i].reverse()

    return matrix
