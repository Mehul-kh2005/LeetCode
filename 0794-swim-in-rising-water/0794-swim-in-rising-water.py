class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def possible(mid):
            seen = set()
            
            def dfs(r, c):
                if r == m-1 and c == n-1:
                    return True
                seen.add((r, c))
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                        if grid[nr][nc] <= mid:
                            if dfs(nr, nc):
                                return True
                return False
            
            return grid[0][0] <= mid and dfs(0, 0)
        
        def binary_search():
            lo, hi = grid[0][0], max(max(row) for row in grid)
            while lo < hi:
                mid = (lo + hi) // 2
                if possible(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        return binary_search()