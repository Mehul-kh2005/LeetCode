class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        count=0

        for i in range(1,n):
            if nums[i]<nums[i-1]:
                if count or (i>1 and i<n-1 and nums[i]<nums[i-2] and nums[i+1]<nums[i-1]):
                    return False
                count+=1
        
        return True