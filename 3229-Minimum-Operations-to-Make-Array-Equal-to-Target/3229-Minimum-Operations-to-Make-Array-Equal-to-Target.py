class Solution:
    def minimumOperations(self, nums: List[int], t: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            t[i] -= nums[i]
        
        t = [0] + t + [0]
        
        total = 0
        for i in range(1, n+2):
            total += abs(t[i] - t[i-1])

        return total//2