#!/usr/bin/python3

def generate_pascals_triangle(n):
    """
    Generate Pascal's triangle with n rows.

    Args:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    List[List[int]]: A list of lists representing Pascal's triangle.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]  # First row is always [1]

    # Generate each row of the triangle
    for _ in range(1, n):
        last_row = triangle[-1]  # Get the last row of the triangle
        row = [1]  # Start the new row with a 1

        # Calculate the intermediate values of the new row
        row.extend([
            last_row[j] + last_row[j + 1]
            for j in range(len(last_row) - 1)
        ])

        # End the new row with a 1
        row.append(1)

        # Append the new row to the triangle
        triangle.append(row)

    return triangle
