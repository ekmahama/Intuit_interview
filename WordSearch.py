def findWord(board, word):
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            if backtrack(i,j,word):
                return True
    return False

    def backtrack(i, j, word):
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if len(word) == 0:
            return True
        # check for out of bounds
        if i < 0 or i == rows or j < 0 or j == rows:
            return False

        # check if first charater matches
        if word[0] != board[i][j]:
            return False
        ret = False

        # Mark visited cell
        board[i][j] = '#'
        for rowOffset, colOffset in steps:
            ret = backtrack(i+rowOffset, j + colOffset, word[1:])
            if ret:
                break

        # backtrack
        board[i][j] = word[0]
        return ret
