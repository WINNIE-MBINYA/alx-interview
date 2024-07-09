#!/usr/bin/python3
"""
Module for minOperations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
