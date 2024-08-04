class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n=len(nums)
        subarrays=[]
        
        for i in range(n):
            for j in range(i,n):
                subarrays.append(sum(nums[i:j+1]))
        
        subarrays.sort()
        return sum(subarrays[left-1:right])%(10**9+7)