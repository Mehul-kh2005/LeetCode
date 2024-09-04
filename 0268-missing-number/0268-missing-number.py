class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        seen=[False]*(n+1)

        for num in nums:
            if 0<=num<=n:
                seen[num]=True

        for i in range(n+1):
            if not seen[i]:
                return i

        return i+1