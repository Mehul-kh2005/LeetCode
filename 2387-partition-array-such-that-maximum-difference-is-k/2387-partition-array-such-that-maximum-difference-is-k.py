class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=1
        start=nums[0]

        for i in range(1,len(nums)):
            if nums[i]-start>k:
                count+=1
                start=nums[i]

        return count