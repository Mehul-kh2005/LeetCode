class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        rowPos=[]
        colPos=[]

        for row in range(n):
            for col in range(m):
                if matrix[row][col]==0:
                    rowPos.append(row)
                    colPos.append(col)

        for row,col in zip(rowPos,colPos):
            for i in range(n):
                matrix[i][col]=0

            for j in range(m):
                matrix[row][j]=0