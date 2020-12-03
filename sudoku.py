def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    r, c = findUassigned(board)
    if r == -1 and c == -1:
        return True
    for num in [str(i) for i in range(1, 10)]:
        if canPlace(r, c, num, board):
            board[r][c] = num

            if solveSudoku(board):
                return True
            board[r][c] = '.'
    return False


def findUassigned(board):
    row, col = len(board), len(board[0])
    for r in range(row):
        for c in range(col):
            if board[r][c] == '.':
                return r, c

    return -1, -1


def canPlace(i, j, num, board):

    # Check it row placement is possible
    if any([num == n for n in board[i]]):
        return False

    # check if column placement is possibe
    if any([num == n for n in [row[j] for row in board]]):
        return False

    # check if subboard placment in possible
    row, col = (i//3)*3, (j//3)*3
    for r in range(row, row + 3):
        for c in range(col, col+3):
            if board[r][c] == num:
                return False

    return True
