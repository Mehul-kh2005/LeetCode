class Solution:
    def check(self, nums: List[int]) -> bool:
        inversion_count=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                inversion_count+=1

        if nums[0]<nums[-1]:
            inversion_count+=1
            
        return inversion_count<=1