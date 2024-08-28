class Solution:
    directions=[(0,1),(1,0),(0,-1),(-1,0)]

    def is_cell_land(self,x,y,grid):
        return grid[x][y]==1

    def is_sub_island(self,x,y,grid1,grid2,rows,cols,visited):
        is_sub_island=True
        pending_cells=deque()

        pending_cells.append((x,y))
        visited[x][y]=True

        while pending_cells:
            curr_x,curr_y=pending_cells.popleft()

            if not self.is_cell_land(curr_x,curr_y,grid1):
                is_sub_island=False

            for direction in self.directions:
                next_x=curr_x+direction[0]
                next_y=curr_y+direction[1]

                if (
                    0<=next_x<rows 
                    and 0<=next_y<cols 
                    and not visited[next_x][next_y] 
                    and self.is_cell_land(next_x,next_y,grid2)
                ):
                    pending_cells.append((next_x,next_y))
                    visited[next_x][next_y]=True

        return is_sub_island
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows=len(grid2)
        cols=len(grid2[0])

        visited=[[False]*cols for _ in range(rows)]
        sub_island_count=0

        for x in range(rows):
            for y in range(cols):
                if (
                    not visited[x][y] 
                    and self.is_cell_land(x,y,grid2) 
                    and self.is_sub_island(x,y,grid1,grid2,rows,cols,visited)):
                    sub_island_count+=1

        return sub_island_count