class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        result=0

        for i in range(n-2):
            mid=nums[i+1]

            if mid%2!=0:
                continue

            if mid//2==nums[i]+nums[i+2]:
                result+=1

        return result