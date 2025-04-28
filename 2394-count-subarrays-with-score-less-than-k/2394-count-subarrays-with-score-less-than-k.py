class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        curr_sum,result=0,0
        i=0        
        
        for j in range(n):
            curr_sum+=nums[j]

            while i<=j and curr_sum*(j-i+1)>=k:
                curr_sum-=nums[i]
                i+=1

            result+=j-i+1

        return result