class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result=[]
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        steps=1
        direction=0
        row,col=rStart,cStart
        result.append([row,col])

        while len(result)<rows*cols:
            for _ in range(2):
                for _ in range(steps):
                    row+=dir[direction][0]
                    col+=dir[direction][1]

                    if 0<=row<rows and 0<=col<cols:
                        result.append([row,col])

                direction=(direction+1)%4
            steps+=1

        return result