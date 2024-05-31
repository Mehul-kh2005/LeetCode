class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor2no = 0
        for num in nums:
            xor2no ^= num

        lowestBit = xor2no & -xor2no

        result = [0, 0]
        for num in nums:
            if (lowestBit & num) == 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result