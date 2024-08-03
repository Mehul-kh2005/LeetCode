class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        # rows first
        ans_row = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            c = 0
            for j in range(m):
                if(grid[i][j] != grid[i][m - j - 1]):
                    c += 1
            ans_row += c // 2
        # col next
        ans_col = 0
        for j in range(m):
            c = 0
            for i in range(n):
                if(grid[i][j] != grid[n - i - 1][j]):
                    c += 1
            ans_col += c // 2
        return min(ans_row, ans_col)