class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start==len(nums):
                perm=tuple(nums)
                if perm not in seen:
                    seen.add(perm)
                    result.append(nums[:])
                return
            
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                backtrack(start+1)
                nums[start],nums[i]=nums[i],nums[start]

        result=[]
        seen=set()
        nums.sort
        backtrack(0)
        return result