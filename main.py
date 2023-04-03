#!/usr/bin/env python3

import random
import print_grid

# function to update the grid after each generations
def update_grid(grid_struc):
    # get length of grid's row and colums
    ROWS = len(grid_struc)
    COLS = len(grid_struc[0])

    # new 2x2 grid to be updated
    # all cells initialized to zero
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]





if __name__ == "__main__":
    random.seed(1)

    # row and colums
    ROWS = 5
    COLS = 5

    # grid to create a 5x5 2-D matrix of random numbers between 0 and 1
    grid = [[random.randint(0, 1) for _ in range(ROWS)] for _ in range(COLS)]

    # print grid in original form (2x2 matrix)
    for i in grid:
        print(i)

    print()

    # testing print_grid() method imported from print_grid module
    print_grid.print_grid(grid)
