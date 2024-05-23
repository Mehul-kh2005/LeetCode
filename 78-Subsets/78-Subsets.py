class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,path):
            subsets.append(path)
            for i in range(start,len(nums)):
                backtrack(i+1,path+[nums[i]])
        subsets=[]
        backtrack(0,[])
        return subsets