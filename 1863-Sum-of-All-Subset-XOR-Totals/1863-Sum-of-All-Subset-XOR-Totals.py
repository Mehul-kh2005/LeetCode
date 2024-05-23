class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start,path):
            subsets.append(path)
            for i in range(start,len(nums)):
                backtrack(i+1,path+[nums[i]])
        subsets=[]
        backtrack(0,[])
        
        result=0
        for subset in subsets:
            subset_XOR_total=0
            for num in subset:
                subset_XOR_total^=num
            result+=subset_XOR_total
        return result