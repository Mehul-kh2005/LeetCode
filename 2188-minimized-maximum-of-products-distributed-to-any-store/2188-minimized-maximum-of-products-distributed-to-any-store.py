class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left,right=1,max(quantities)

        def can_distribute(x):
            stores_needed=sum(math.ceil(q/x) for q in quantities)
            return stores_needed<=n

        while left<right:
            mid=(left+right)//2
            if can_distribute(mid):
                right=mid
            else:
                left=mid+1

        return left