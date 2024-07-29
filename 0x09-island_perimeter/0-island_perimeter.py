#!/usr/bin/python3
"""island module"""


def island_perimeter(grid):
    """
    Defines function too find perimter of a grid
    land[1] and water[0]
    Args:
       grid [list]: List of integers
    """
    rows = len(grid)
    col = len(grid[0])

    perimeter = 0

    for x in range(rows):
        for y in range(col):
            # check if it is land
            if grid[x][y] == 1:
                # check if it is water
                if x == 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                # check if below is water
                if x == rows - 1 or grid[x + 1][y] == 0:
                    perimeter += 1
                # check if left is water
                if y == 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                # check if right is water
                if y == col - 1 or grid[x][y+1] == 0:
                    perimeter += 1
    return perimeter
