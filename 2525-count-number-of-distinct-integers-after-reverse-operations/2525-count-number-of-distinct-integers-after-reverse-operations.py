class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_cop = nums.copy()
        for i in nums_cop:
            nums.append(int(str(i)[::-1]))
        
        return (len(set(nums)))