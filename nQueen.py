def Nqueen(board, N):
    if N == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if isAttacked(i, j, board, N):
                continue
            board[i][j] = 1
            if Nqueen(board, N-1):
                return True
            board[i][j] = 0

    return False


def isAttacked(x, y, board, N):
    # check if there is 1 on the xth row
    for i in range(len(board)):
        if board[x][i] == 1:
            return True
    for j in range(len(board[0])):
        if board[j][y] == 1:
            return True
    for m in range(len(board)):
        for n in range(len(board[0])):
            if (m + n) == (x+y) and board[m][n] == 1:
                return True
            elif (m-n) == (x-y) and board[m][n] == 1:
                return True
    return False


N = 4
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
ret = Nqueen(board, N)
print()
