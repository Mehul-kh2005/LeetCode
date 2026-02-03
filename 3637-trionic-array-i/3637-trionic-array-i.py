class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] >= nums[1]:
            return False

        count = 1
        for i in range(2, n):
            if nums[i - 1] == nums[i]:
                return False
            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0:
                count += 1

        return count == 3