class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col, result, prev = len(matrix), len(matrix[0]), 0, 0
        dp = [0 for _ in range(col + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == 1:
                    temp = dp[j]
                    dp[j] = 1 + min(prev, min(dp[j - 1], dp[j]))
                    prev = temp
                    result += dp[j]
                else:
                    dp[j] = 0

        return result