class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal=float('-inf')
        prefix=suffix=1
        n=len(nums)

        for i in range(n):
            if prefix==0:
                prefix=1

            if suffix==0:
                suffix=1

            prefix*=nums[i]
            suffix*=nums[n-i-1]
            maxVal=max(maxVal,max(prefix,suffix))

        return maxVal