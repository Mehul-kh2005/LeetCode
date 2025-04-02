class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max,total_max=0,0

        for num in nums:
            if num==1:
                curr_max+=1
            total_max=max(total_max,curr_max)

            if num!=1:
                curr_max=0        

        return total_max