class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                c+=1
            if c>1:
                return False
        return True