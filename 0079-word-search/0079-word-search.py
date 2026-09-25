class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(board) == 0:
            return False

        top = 0
        left = 0
        bottom = len(board) - 1
        right = len(board[0]) - 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(board, word, i, j, 0):
                        return True

        return False

    def search(self, board, word, row, col, index):
        if index == len(word):
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"

        found = (
            self.search(board, word, row + 1, col, index + 1) or
            self.search(board, word, row - 1, col, index + 1) or
            self.search(board, word, row, col + 1, index + 1) or 
            self.search(board, word, row, col - 1, index + 1)
        )
        board[row][col] = temp

        return found
