class neighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        # Create a map to store the position of each value
        self.value_to_pos = {grid[i][j]: (i, j) for i in range(self.n) for j in range(self.n)}

    def adjacentSum(self, value: int) -> int:
        if value not in self.value_to_pos:
            return 0
        
        x, y = self.value_to_pos[value]
        adjacent_sum = 0
        
        # Possible adjacent directions: top, bottom, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                adjacent_sum += self.grid[nx][ny]
        
        return adjacent_sum

    def diagonalSum(self, value: int) -> int:
        if value not in self.value_to_pos:
            return 0
        
        x, y = self.value_to_pos[value]
        diagonal_sum = 0
        
        # Possible diagonal directions: top-left, top-right, bottom-left, bottom-right
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                diagonal_sum += self.grid[nx][ny]
        
        return diagonal_sum



# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)