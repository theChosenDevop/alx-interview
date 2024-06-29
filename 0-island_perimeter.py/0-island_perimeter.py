#!/usr/bin/python3
"""island module"""

def island_perimeter(grid):
    """
    Defines function too find perimter of a grid
    Args:
       grid [list]: List of integers
    """
    grid_len = len(grid)
    count = 0
    y = [[count := count + 1 for row in grid if row[i] == 1] for i in range(grid_len)]
    return y
