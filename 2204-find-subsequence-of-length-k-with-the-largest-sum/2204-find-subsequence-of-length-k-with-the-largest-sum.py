class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new_nums=[(i,val) for i,val in enumerate(nums)]
        
        new_nums=sorted(new_nums,key=lambda x:x[1],reverse=True)[:k]

        new_nums.sort(key=lambda x:x[0])

        return [val for i,val in new_nums]