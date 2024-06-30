def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1]  # First element is always 1
        if triangle:  # Only proceed if there are rows already in the triangle
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # Last element is always 1
        triangle.append(row)
    
    return triangle
