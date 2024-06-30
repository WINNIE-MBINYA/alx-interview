#!/usr/bin/python3

"""
This script contains a function to generate Pascal's triangle.

Pascal's triangle is a triangular array of the binomial coefficients.
Each row represents the coefficients of the binomial expansion.
"""

def generate_pascals_triangle(n):
    """
    Generate Pascal's triangle with n rows.

    Args:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    List[List[int]]: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for _ in range(1, n):
        last_row = triangle[-1]
        row = [1]
        row.extend([
            last_row[j] + last_row[j + 1]
            for j in range(len(last_row) - 1)
        ])
        row.append(1)
        triangle.append(row)

    return triangle
