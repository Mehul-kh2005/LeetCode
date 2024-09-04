class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a=[str(num) for num in nums]
        b=[int(a[i][::-1]) for i in range(len(nums))]
        nums=set(nums+b)
        return len(nums)