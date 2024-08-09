class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(matrix):
            numbers = matrix[0] + matrix[1] + matrix[2]
            if sorted(numbers) != list(range(1, 10)):
                return False
                
            return (len(matrix)==3 and all(len(row)==3 for row in matrix) and 
            len(set(matrix[0]+matrix[1]+matrix[2]))==9 and 
            sum(matrix[0])==15 and 
            sum(matrix[1])==15 and
            sum(matrix[2])==15 and
            sum(matrix[i][0] for i in range(3))==15 and 
            sum(matrix[i][1] for i in range(3))==15 and
            sum(matrix[i][2] for i in range(3))==15 and
            sum(matrix[i][i] for i in range(3))==15 and
            sum(matrix[i][2-i] for i in range(3))==15)

        rows,cols=len(grid),len(grid[0])
        if rows<3 or cols<3:
            return 0
        
        count=0

        for i in range(rows-2):
            for j in range(cols-2):
                subgrid=[row[j:j+3] for row in grid[i:i+3]]
                if isMagicSquare(subgrid):
                    count += 1

        return count