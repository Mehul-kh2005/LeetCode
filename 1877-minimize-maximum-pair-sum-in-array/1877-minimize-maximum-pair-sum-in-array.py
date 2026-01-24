class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        min_val, max_val = float('inf'), float('-inf')
        freq = [0] * 100001
        for i in range (len(nums)):
            if nums[i] < min_val: min_val = nums[i]
            if nums[i] > max_val: max_val = nums[i]
            freq[nums[i]] += 1
        max_sum, l, r = 0, min_val, max_val
        while l <= r:
            if freq[l] == 0: l += 1
            elif freq[r] == 0: r -= 1
            else:
                max_sum = max(max_sum, l + r)
                freq[l] -= 1
                freq[r] -= 1
        return max_sum