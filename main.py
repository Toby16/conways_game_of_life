#!/usr/bin/env python3

import random
from print_grid import print_grid





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
