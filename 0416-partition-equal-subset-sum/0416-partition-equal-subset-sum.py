class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False

        n=total_sum//2
        dp=set([0])

        for num in nums:
            new_dp=dp.copy()

            for x in dp:
                if x+num==n:
                    return True
                new_dp.add(x+num)
            dp=new_dp

        return False