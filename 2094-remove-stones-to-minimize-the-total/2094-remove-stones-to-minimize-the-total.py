import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-pile for pile in piles]
        heapq.heapify(piles)

        while k!=0:
            max_ele=-heapq.heappop(piles)
            remaining_stones=max_ele-(max_ele//2)  
            heapq.heappush(piles,-remaining_stones)
            k-=1

        return -sum(piles)