class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0

        low,high=0,n-1

        while low<high:
            mid=(low+high)>>1

            if nums[mid-1]<=nums[mid]>=nums[mid+1]:
                return mid

            elif nums[mid+1]>nums[mid]:
                low=mid+1

            else:
                high=mid-1

        return low