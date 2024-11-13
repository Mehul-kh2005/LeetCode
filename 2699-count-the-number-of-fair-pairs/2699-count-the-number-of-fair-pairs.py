class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums,upper+1)-self.lower_bound(nums,lower)

    def lower_bound(self,nums,value):
        left,right=0,len(nums)-1
        result=0

        while left<right:
            sum1=nums[left]+nums[right]

            if sum1<value:
                result+=right-left
                left+=1
            else:
                right-=1

        return result