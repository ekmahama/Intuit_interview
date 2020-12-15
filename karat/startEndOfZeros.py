from collections import deque


def startEndOfZeros(grid):
    result = []
    if not grid or not grid[0]:
        return result
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                end = BFS(grid, i, j)
                result.append([[i, j], end])
                # return result

    return result


def BFS(grid, i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for nr, nc in [(x+1, y), (x, y+1)]:
            if grid[nc][nr] == 0:
                grid[nc][nr] = 2
                q.append((nc, nr))
    return [x, y]


def DFS(grid, i, j):
    res = []
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1:
        return res
    for nr, nc in ([i+1, j], [i, j+1]):
        res += DFS(grid, nr, nc)


grid = [[1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]]
res = startEndOfZeros(grid)
print(res)
