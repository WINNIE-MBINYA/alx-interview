#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows of Pascal's triangle to generate.

    Returns:
        list of lists: A list containing lists of integers representing each row
                       of Pascal's triangle up to the nth row. Returns an empty list
                       if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row of Pascal's triangle
    
    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            """Calculate each element based on the previous row"""
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the row to the triangle
    
    return triangle
