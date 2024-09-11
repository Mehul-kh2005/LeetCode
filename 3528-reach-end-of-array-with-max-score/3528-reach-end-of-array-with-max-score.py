class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans=max_score=0

        for num in nums:
            ans+=max_score
            max_score=max(max_score,num)

        return ans