#!/usr/bin/python3
"""
This module contains the function rotate_2d_matrix
which rotates an n x n 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the matrix in place 90 degrees clockwise.

    Args:
        matrix (list of lists): A 2D list to be rotated.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
