def solve(board):
    if not board or not board[0]:
        return board
    rows, cols = len(board), len(board[0])

    def DFS(board, i, j):
        # check for out of bounds
        if i < 0 or i >= len(board):
            return
        if board[i][j] != 'O':
            return

        # Mark cell as escaped
        board[i][j] = 'E'
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            DFS(board, i+x, j+y)
    # DFS starting from upper row  and lower row
    for j in range(cols):
        if board[0][j] == 'O':
            DFS(board, 0, j)
        if board[rows - 1][j] == 'O':
            DFS(board, rows-1, j)

    # DFS for left and right edges
    for i in range(cols):
        if board[i][0] == 'O':
            DFS(board, i, 0)
        if board[i][cols-1] == 'O':
            DFS(board, i, cols-1)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solve(board)
print()
