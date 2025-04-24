from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        freq=defaultdict(int)
        right=0
        unique_elements=len(set(nums))
        count=0

        for left in range(n-unique_elements+1):
            if left>0:
                remove=nums[left-1]
                freq[remove]-=1

                if freq[remove]==0:
                    del freq[remove] 

            while right<n and len(freq)<unique_elements:
                freq[nums[right]]+=1
                right+=1

            if len(freq)==unique_elements:
                count+=n-right+1

        return count