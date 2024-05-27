class Solution:
    def specialArray(self, nums: List[int]) -> int:
        bucket=[0]*1001
        for num in nums:
            bucket[num]+=1  
        total=len(nums)        
        for i in range(1001):
            if i==total:
                return i
            total-=bucket[i]       
        return -1