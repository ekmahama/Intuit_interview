from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.counter = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        for i, x in enumerate((row, col, row+col, row-col)):
            self.counter[i, x, player] += 1
            if self.counter[i, x, player] == self.n:
                return player
        return 0


