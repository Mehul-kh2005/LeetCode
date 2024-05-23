class Solution:
    def maxElement(self,grid,i,j):
        max_element=0
        for row in range(i,i+3):
            for col in range(j,j+3):
                max_element=max(max_element,grid[row][col])
        return max_element

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        matrix=[[0 for j in range(n-2)] for i in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                matrix[i][j]=self.maxElement(grid,i,j)
        return matrix