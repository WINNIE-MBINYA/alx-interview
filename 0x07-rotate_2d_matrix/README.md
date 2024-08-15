# Rotate 2D Matrix

This project contains a Python function to rotate an `n x n` 2D matrix 90 degrees clockwise in place.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Files](#files)
- [Author](#author)

## Description

Given an `n x n` 2D matrix, the goal is to rotate it 90 degrees clockwise. The rotation should be performed in place, meaning no additional data structures are used to hold the matrix elements during the rotation.

## Requirements

- The code is written in Python 3.8.10.
- The code adheres to the [Pycodestyle](https://pycodestyle.pycqa.org/en/latest/) style guide (version 2.8.0).
- No external libraries are used.
- The function does not return anything; it modifies the matrix in place.
- The matrix provided will always have 2 dimensions and will not be empty.

## Usage

To use the function, simply import it and pass a 2D list (matrix) as an argument. The matrix will be rotated in place.

```python
#!/usr/bin/python3
"""
Example usage of rotate_2d_matrix function.
"""

rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    rotate_2d_matrix(matrix)
    print(matrix)
