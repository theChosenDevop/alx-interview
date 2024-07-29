#!/usr/bin/python3
"""
    N Queens Challenge
"""
import sys


def is_safe(placed_queens, r, c):
    """
    Determines if a queen can be placed at row `r` and column `c` without
    being attacked by any previously placed queens.

    Parameters:
        placed_queens (list): List of tuples representing the positions
        of previously placed queens.
        r (int): The row where the queen is to be placed.
        c (int): The column where the queen is to be placed.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for qr, qc in placed_queens:
        if qc == c or abs(qr - r) == abs(qc - c):
            return False
    return True


def solve_n_queens(n):
    """
    Solves the N Queens problem and returns all possible solutions.

    Parameters:
        n (int): The size of the board (n x n) and
        the number of queens to place.

    Returns:
        list: A list of solutions, where each solution is
        represented by a list of tuples.
        Each tuple contains the row and column positions of a queen.
    """
    def backtrack(r):
        """
        Recursively places queens on the board and backtracks
        if a solution is not found.

        Parameters:
            r (int): The current row where a queen is to be placed.
        """
        if r == n:
            solutions.append(placed_queens[:])
            return
        for c in range(n):
            if is_safe(placed_queens, r, c):
                placed_queens.append((r, c))
                backtrack(r + 1)
                placed_queens.pop()

    solutions = []
    placed_queens = []
    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)

    for solution in solutions:
        print(solution)
