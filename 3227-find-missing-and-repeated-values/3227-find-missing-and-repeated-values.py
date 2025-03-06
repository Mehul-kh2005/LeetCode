class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        num_sum=0
        squared_sum=0
        total=n*n

        for i in range(n):
            for j in range(n):
                num_sum+=grid[i][j]
                squared_sum+=grid[i][j]**2

        sum_diff=num_sum-total*(total+1)//2
        sqr_diff=squared_sum-total*(total+1)*(2*total+1)//6

        repeat=(sqr_diff//sum_diff+sum_diff)//2
        missing=(sqr_diff//sum_diff-sum_diff)//2

        return [repeat,missing]