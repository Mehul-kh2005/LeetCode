class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        xor_product = 0

        for i in range(len(nums)):

            xor_product = xor_product ^ nums[i]

        ans = [0] * len(nums)

        mask = (1 << maximumBit) - 1

        for i in range(len(nums)):

            ans[i] = xor_product ^ mask

            # remove last element

            xor_product = xor_product ^ nums[len(nums) - 1 - i]

        return ans