from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isPossible(k):
            time_taken=0
            for pile in piles:
                time_taken+=ceil(pile/k)

            return time_taken<=h

        left=1
        right=max(piles)

        while left<=right:
            mid=(left+right)//2

            if isPossible(mid):
                right=mid-1
            else:
                left=mid+1

        return left