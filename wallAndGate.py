def wallsAndGate(rooms):
    if not rooms or not rooms[0]:
        return
    numRows, numCols = len(rooms), len(rooms[0])

    for i in range(numRows):
        for j in range(numCols):
            if rooms[i][j] == 0:
                DFS(rooms, i, j, 0)


def DFS(rooms, i, j, dist):
    if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or dist > rooms[i][j]:
        return
    rooms[i][j] = dist

    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        DFS(rooms, i+x, y+j, dist+1)


rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
wallsAndGate(rooms)
