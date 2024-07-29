#!/usr/bin/python3
"""Minimum operations module"""


def minOperations(n):
    """ Calculates the minimum number of operations
        to reach n characters
    """
    if n <= 1:
        return 0

    operations = 0
    div = 2

    while n > 1:
        if n % div == 0:
            n //= div
            operations += div
        else:
            div += 1

    return operations
