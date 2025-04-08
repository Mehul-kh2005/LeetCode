class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        elements_set=set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in elements_set:
                return (i//3)+1
            elements_set.add(nums[i])
            
        return 0