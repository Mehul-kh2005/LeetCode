class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def count_flips(sequence):
            return sum(1 for i in range(len(sequence) // 2) if sequence[i] != sequence[~i])

        rows = [count_flips(row) for row in grid]
        cols = [count_flips([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]

        return min(sum(rows), sum(cols))