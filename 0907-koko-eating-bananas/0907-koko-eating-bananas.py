class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)

        def can_finish(n):
            hours_needed=sum(math.ceil(p/n) for p in piles)
            return hours_needed<=h

        while left<right:
            mid=(left+right)//2
            if can_finish(mid):
                right=mid
            else:
                left=mid+1

        return left