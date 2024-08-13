class Solution:
    def check(self, nums: List[int]) -> bool:
        lst=sorted(nums.copy())

        for i in range(len(nums)):
            nums[:]=nums[-1:]+nums[:-1]
            if lst==nums:
                return True
        return False