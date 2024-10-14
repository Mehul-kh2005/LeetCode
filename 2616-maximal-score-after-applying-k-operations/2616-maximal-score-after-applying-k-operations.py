import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[]
        score=0
        for num in nums:
            heapq.heappush(heap,-1*num)

        while k!=0:
            max_ele=-1*heapq.heappop(heap)
            score+=max_ele
            heapq.heappush(heap,-1*ceil(max_ele/3))
            k-=1

        return score