class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result,i_max,j_max=0,0,0

        for k in range(len(nums)):
            result=max(result,j_max*nums[k])
            j_max=max(j_max,i_max-nums[k])
            i_max=max(i_max,nums[k])

        return result