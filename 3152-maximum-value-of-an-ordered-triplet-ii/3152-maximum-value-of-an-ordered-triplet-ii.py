class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i_index,j_index,result=0,0,0

        for i in range(len(nums)):
            result=max(result,j_index*nums[i])
            j_index=max(j_index,i_index-nums[i])
            i_index=max(i_index,nums[i])

        return result