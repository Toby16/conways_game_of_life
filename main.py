#!/usr/bin/env python3

import random
import print_grid

# function to update the grid after each generations
def update_grid(grid_struc):
    # get length of grid's row and colums
    ROWS = len(grid_struc)
    COLS = len(grid_struc[0])

    # new 2x2 matrix to be updated
    # all cells initialized to zero
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    # loop through the 2x2 matrix to access each cell
    for row in range(ROWS):
        for col in range(COLS):
            # initialize a counter to count amount of neighbors of a cell
            count = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i == 0) and (j == 0):
                        # grid_struc[row+1][col+j]
                        # grid_struc[row+0][col+0] points the the cell itself
                        continue
                    if ((row + i) < 0) or ((row + i) >=ROWS):
                        # edge case to avoid index error and wrong accessing of neighbors based on rows
                        continue
                    if ((col + j) < 0) or ((col + j) >= COLS):
                        # edge case to avoid index error and wrong accessing of neighbors based on colunms
                        continue
                    count += grid_struc[row + i][col + j]

            """
            RULES
            """
            # Any dead cell with three live neighbours becomes a live cell
            if grid_struc[row][col] == 0:
                if count == 3:
                    new_grid[row][col] = 1
            # Live cell
            if grid_struc[row][col] == 1:
                # Any live cell with two or three live neighbours survives
                if count in [2, 3]:
                    new_grid[row][col] = 1
    
    return (new_grid)





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
    # print_grid.print_grid(grid)

    print()

    grid_test = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0]
            ]

    print_grid.print_grid(grid_test)

    # testing updating function
    for i in range(5):
        grid_test = update_grid(grid_test)
        print()
        print("GENERATION:", i + 1)
        print_grid.print_grid(grid_test)

