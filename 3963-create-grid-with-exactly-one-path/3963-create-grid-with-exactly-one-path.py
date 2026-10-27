class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        for i in range(m):
            if i % 2 == 0:
                for j in range(n):
                    grid[i][j] = '.'
            else:
                grid[i][n - 1] = '.'

        grid[m - 1][n - 1] = '.'

        return [''.join(row) for row in grid]