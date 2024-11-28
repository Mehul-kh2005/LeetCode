class Solution:       
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def isValid(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(grid)
        n=len(grid[0])

        minimumObstacles=[[float('inf')]*n for _ in range(m)]
        minimumObstacles[0][0]=0
        dq=deque([(0,0,0)])

        while dq:
            obstacle,row,col=dq.popleft()

            if (row,col)==(m-1,n-1):
                return obstacle

            for dr,dc in directions:
                new_row,new_col=row+dr,col+dc

                if isValid(new_row,new_col) and minimumObstacles[new_row][new_col]==float('inf'):
                    if grid[new_row][new_col]==1:
                        minimumObstacles[new_row][new_col]=obstacle+1
                        dq.append((obstacle+1,new_row,new_col))
                        
                    else:
                        minimumObstacles[new_row][new_col]=obstacle
                        dq.appendleft((obstacle,new_row,new_col))