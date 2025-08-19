class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt, streak = 0, 0
        for num in nums:
            if num == 0:
                streak += 1
                cnt += streak
            else:
                streak = 0
        return cnt