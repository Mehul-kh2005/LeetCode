class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        
        i=j=0
        curr_d=0
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        lst=[num for num in range(1,(n**2)+1)]
        result=[[0]*n for _ in range(n)]

        for num in lst:
            result[i][j]=num

            new_i=i+directions[curr_d][0]
            new_j=j+directions[curr_d][1]

            if(new_i>=n or new_j>=n or result[new_i][new_j]!=0):
                curr_d=(curr_d+1)%4

            i+=directions[curr_d][0]
            j+=directions[curr_d][1]

        return result