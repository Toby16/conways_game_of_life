#!/usr/bin/env python3

"""
NOTE: this is for testing the game's logic only
"""


def print_grid(grid_struc):
    """
    Prints a 2D grid structure to the console.
    Args:
        grid_struc (list[list[int]]): A 2D list representing the grid.
    """
    for row in grid_struc:
        # Initialize an empty string to represent the current row.
        row_str = ""
        # Iterate over each cell in the current row.
        for cell in row:
            """
            Convert the cell value to a string,
            append it to the current row string,
            followed by a space.
            """
            row_str += str(cell) + " "
        print(row_str)


if __name__ == "__main__":
    import random

    grid = [[random.randint(0, 1) for _ in range(5)] for _ in range(10)]
    print_grid(grid)
