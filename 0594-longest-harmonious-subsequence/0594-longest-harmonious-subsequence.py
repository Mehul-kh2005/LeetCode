class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq=Counter(nums)
        result=0

        for num in freq:
            if num+1 in freq:
                result=max(result,freq[num]+freq[num+1])

        return result