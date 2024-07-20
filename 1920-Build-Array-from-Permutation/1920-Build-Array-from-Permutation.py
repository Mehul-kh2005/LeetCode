class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_list=[]
        n=len(nums)
        for i in range(0,n):
            new_list.append(nums[nums[i]])
        return new_list