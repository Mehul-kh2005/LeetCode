from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possibleDivisor(k):
            quotient=0
            for num in nums:
                quotient+=ceil(num/k)

            return quotient<=threshold

        left=1
        right=max(nums)
        ans=0

        while left<=right:
            mid=(left+right)//2

            if possibleDivisor(mid):
                ans=mid
                right=mid-1

            else:
                left=mid+1

        return ans