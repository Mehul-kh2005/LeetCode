class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m=len(box)
        n=len(box[0])
        result=[[0]*m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][i]=box[i][j]

        for row in result:
            row.reverse()

        for j in range(m):
            lowestRowWithEmptyCell=n-1

            for i in range(n-1,-1,-1):
                if result[i][j]=='#':
                    result[i][j]='.'
                    result[lowestRowWithEmptyCell][j]='#'
                    lowestRowWithEmptyCell-=1
                    
                if result[i][j]=='*':
                    lowestRowWithEmptyCell=i-1

        return result