def generate_pascals_triangle(n):
    """Generate Pascal's triangle with n rows."""
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
