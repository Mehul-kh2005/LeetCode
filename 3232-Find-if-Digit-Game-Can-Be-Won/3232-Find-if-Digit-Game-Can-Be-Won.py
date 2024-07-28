class Solution:
    def canAliceWin(self, nums):
        sum1 = 0
        sum2 = 0
        for x in nums:
            if x < 10:
                sum1 += x
            else:
                sum2 += x
        return sum1 != sum2