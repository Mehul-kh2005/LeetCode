class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        invert_pair = []

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                invert_pair.append([i - 1, i])

                if len(invert_pair) == 2:
                    return False

        if len(invert_pair) == 1:
            [l, r] = invert_pair[0]
            return l == 0 or nums[l - 1] < nums[r] or r == len(nums) - 1 or nums[l] < nums[r + 1]

        return True