#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of lists representing the grid,
                                    where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Start with a perimeter of 4 for each land cell
                perimeter += 4

                # Check if the cell above is land and subtract 1 if true
                if row > 0 and grid[row - 1][col] == 1:
                    # Since they share a side, subtract from both cells
                    perimeter -= 2

                # Check if the cell to the left is land and subtract 1 if true
                if col > 0 and grid[row][col - 1] == 1:
                    # Since they share a side, subtract from both cells
                    perimeter -= 2

    return perimeter
