"""
Day 44 - Number of Islands

Problem:
Given a 2D grid of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.

Example:

Input:

1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Output:
3
"""


def dfs(grid, row, col):

    rows = len(grid)
    cols = len(grid[0])

    # Boundary and water check
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    if grid[row][col] == "0":
        return

    # Mark current cell as visited
    grid[row][col] = "0"

    # Visit all four directions
    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)


def num_islands(grid):

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)

    return count


# Test Case 1
# -------------------------

grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("Number of Islands:", num_islands(grid1))


# Test Case 2
# -------------------------

grid2 = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]

print("Number of Islands:", num_islands(grid2))