"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


def numIslands(grid):
    numberOfIsland = 0
    if not grid or not grid[0]:
        return numberOfIsland
    numRows, numCols = len(grid), len(grid[0])
    for i in range(numRows):
        for j in range(numCols):
            if grid[i][j] == '1':
                numberOfIsland += getIslandCnt(grid, i, j)
    return numberOfIsland


def getIslandCnt(grid, i, j):
    # check for boundaries
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    # check for non island
    elif grid[i][j] == '0':
        return 0
    # mark as visited
    grid[i][j] = '0'

    # check for neighboring cells
    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        getIslandCnt(grid, i+x, j+y)
    return 1


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

res = numIslands(grid)
print()
