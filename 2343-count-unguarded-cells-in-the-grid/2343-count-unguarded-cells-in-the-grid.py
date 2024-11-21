class Solution:
    unguarded=0
    guarded=1
    guard=2
    wall=3
    
    def markguarded(self,row,col,grid,m,n):
        for r in range(row-1,-1,-1):
            if grid[r][col]==self.guard or grid[r][col]==self.wall:
                break

            grid[r][col]=self.guarded

        for r in range(row+1,m):
            if grid[r][col]==self.guard or grid[r][col]==self.wall:
                break

            grid[r][col]=self.guarded

        for c in range(col-1,-1,-1):
            if grid[row][c]==self.guard or grid[row][c]==self.wall:
                break

            grid[row][c]=self.guarded

        for c in range(col+1,n):
            if grid[row][c]==self.guard or grid[row][c]==self.wall:
                break

            grid[row][c]=self.guarded

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[self.unguarded]*n for _ in range(m)]

        for guard in guards:
            grid[guard[0]][guard[1]]=self.guard

        for wall in walls:
            grid[wall[0]][wall[1]]=self.wall

        for guard in guards:
            self.markguarded(guard[0],guard[1],grid,m,n)

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==self.unguarded:
                    count+=1

        return count