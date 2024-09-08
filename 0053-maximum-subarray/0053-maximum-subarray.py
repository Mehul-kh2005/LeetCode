class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max=global_max=nums[0]

        for i in range(1,len(nums)):
            
            current_max=max(nums[i],current_max+nums[i])

            global_max=max(global_max,current_max)

        return global_max