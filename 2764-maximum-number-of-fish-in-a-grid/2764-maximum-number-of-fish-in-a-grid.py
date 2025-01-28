class Solution:
    def countFishes(self,grid,visited,row,col,num_rows,num_cols):
        numRows=num_rows
        numCols=num_cols
        fishCount=0
        q=[(row,col)]
        visited[row][col]=True

        rowDirections=[0,0,1,-1]
        colDirections=[1,-1,0,0]

        while q:
            row,col=q.pop(0)
            fishCount+=grid[row][col]

            for i in range(4):
                newRow=row+rowDirections[i]
                newCol=col+colDirections[i]
                if 0<=newRow<numRows and 0<=newCol<numCols and grid[newRow][newCol] and not visited[newRow][newCol]:
                        visited[newRow][newCol]=True
                        q.append((newRow,newCol))
                    
        return fishCount

    def findMaxFish(self, grid: List[List[int]]) -> int:
        numRows=len(grid)
        numCols=len(grid[0])
        result=0
        visited=[[False] * numCols for _ in range(numRows)]

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] and not visited[i][j]:
                    result=max(result,self.countFishes(grid,visited,i,j,numRows,numCols))

        return result