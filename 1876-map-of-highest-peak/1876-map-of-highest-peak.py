class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]

        rows=len(isWater)
        cols=len(isWater[0])

        cell_heights=[[-1 for _ in range(cols)] for _ in range(rows)]
        cell_queue=deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]==1:
                    cell_queue.append((i,j))
                    cell_heights[i][j]=0

        next_layer_height=1

        while cell_queue:
            layer_size=len(cell_queue)

            for _ in range(layer_size):
                current_cell=cell_queue.popleft()

                for d in range(4):
                    neighbor_x=current_cell[0]+dx[d]
                    neighbor_y=current_cell[1]+dy[d]

                    if (self.is_valid(neighbor_x,neighbor_y,rows,cols)) and cell_heights[neighbor_x][neighbor_y]==-1:
                        cell_heights[neighbor_x][neighbor_y]=next_layer_height
                        cell_queue.append((neighbor_x,neighbor_y))
            next_layer_height+=1

        return cell_heights

    def is_valid(self,x,y,rows,cols):
        return 0<=x<rows and 0<=y<cols