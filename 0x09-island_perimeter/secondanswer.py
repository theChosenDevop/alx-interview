#!/usr/bin/python3
"""island module"""


def island_perimeter(grid):
    """
    Defines function too find perimter of a grid
    Args:
       grid [list]: List of integers
    """
    grid_len = len(grid)
    perimeter = 4 * count_ones_in(grid, grid_len)
    return perimeter


def count_ones_in(grid, iter):
    """
    Counts one as land and returns count
    Args:
       grid [List]: Grid of list of integers
       iter [int]: integer
    """
    count = 0
    for i in range(iter):
        for row in grid:
            if row[i] == 1:
                count = count + 1
                break
    return count
