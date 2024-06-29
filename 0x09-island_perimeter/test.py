#!/usr/bin/python3
"""island module"""

def island_perimeter(grid):
    """
    Defines function to find perimeter of a grid
    Args:
       grid [list]: List of integers
    """
    grid_len = len(grid)
    perimeter = calculate_perimeter(grid)
    print(perimeter)

def calculate_perimeter(grid):
    """"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check all four sides of the cell
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[i])-1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1
    return perimeter

# Example usage:
grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
island_perimeter(grid)

