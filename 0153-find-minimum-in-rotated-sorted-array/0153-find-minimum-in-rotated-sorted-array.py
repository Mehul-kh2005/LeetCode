class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        min_value=float('inf')

        while left<=right:
            mid=(left+right)//2

            if nums[left]<=nums[mid]:
                min_value=min(min_value,nums[left])
                left=mid+1

            else:
                min_value=min(min_value,nums[mid])
                right=mid-1

        return min_value