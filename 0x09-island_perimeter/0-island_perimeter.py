#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D list representing the grid.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Found land cell
                # Check the four possible directions (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

