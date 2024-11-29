class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        if grid[0][1]>1 and grid[1][0]>1:
            return -1

        def isValid(visited,row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in visited

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        rows,cols=len(grid),len(grid[0])
        visited=set()
        pq=[(grid[0][0],0,0)]

        while pq:
            time,row,col=heapq.heappop(pq)

            if (row,col)==(rows-1,cols-1):
                return time

            if (row,col) in visited:
                continue
            visited.add((row,col))

            for dx,dy in directions:
                next_row=row+dx
                next_col=col+dy

                if not isValid(visited,next_row,next_col):
                    continue

                wait_time=1 if (grid[next_row][next_col]-time)%2==0 else 0
                next_time=max(grid[next_row][next_col]+wait_time,time+1)
                heapq.heappush(pq,(next_time,next_row,next_col))

        return -1