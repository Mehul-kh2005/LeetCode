from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        same=0
        right=-1
        freq=defaultdict(int)
        ans=0
        n=len(nums)

        for left in range(n):
            while same<k and right+1<n:
                right+=1
                same+=freq[nums[right]]
                freq[nums[right]]+=1

            if same>=k:
                ans+=n-right

            freq[nums[left]]-=1
            same-=freq[nums[left]]

        return ans