class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        curr_max_sum=0
        min_sum=0
        curr_min_sum=0

        for i in range(len(nums)):
            curr_max_sum=max(curr_max_sum+nums[i],nums[i])
            curr_min_sum=min(curr_min_sum+nums[i],nums[i])
            max_sum=max(max_sum,curr_max_sum)
            min_sum=min(min_sum,curr_min_sum)

        return max(max_sum,abs(min_sum))