class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=n*(n+1)//2
        curr_sum=sum(nums)
        return total_sum-curr_sum