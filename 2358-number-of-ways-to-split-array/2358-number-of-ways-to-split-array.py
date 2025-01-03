class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        count=0
        first_split=0

        for i in range(len(nums)-1):
            first_split+=nums[i]
            if first_split>=total_sum-first_split:
                count+=1

        return count