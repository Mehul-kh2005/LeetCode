inf = 10 ** 15
fmax = lambda x, y: x if x > y else y
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        accs = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(n):
            for j in range(m):
                accs[j+1][i+1] = grid[i][j]
        n, m = m, n
        for i in range(n):
            for j in range(m):
                accs[i+1][j+1] += accs[i+1][j]
        
        dp1 = [0] * (m + 1)
        dp2 = [-inf] * (m + 1)
        
        for i in range(1, n + 1):
            ndp1 = [0] * (m + 1)
            ndp2 = [-inf] * (m + 1)
            
            for j in range(m + 1):
                for k in range(j, m + 1):
                    ndp1[k] = fmax(ndp1[k], dp1[j] + accs[i-1][k] - accs[i-1][j])
                    ndp1[k] = fmax(ndp1[k], dp2[0])
                for k in range(j + 1):
                    ndp2[k] = fmax(ndp2[k], dp2[j] + accs[i][j] - accs[i][k])
            ndp2[m] = fmax(ndp2[m], ndp1[m])
            dp1, dp2 = ndp1, ndp2
        return max(max(dp1), max(dp2))