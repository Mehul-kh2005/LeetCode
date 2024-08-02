class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        result=[]
        sliding=deque()

        for i in range(n):
            if sliding and sliding[0]<i-k+1:
                sliding.popleft()

            while sliding and nums[sliding[-1]]<nums[i]:
                sliding.pop()

            sliding.append(i)

            if i>=k-1:
                result.append(nums[sliding[0]])

        return result