class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(capacity):
            curr_day=1
            load=0

            for weight in weights:
                if load+weight>capacity:
                    curr_day+=1
                    load=weight

                else:
                    load+=weight

            return curr_day<=days

        left=max(weights)
        right=sum(weights)

        while left<=right:
            mid=(left+right)//2

            if isPossible(mid):
                right=mid-1

            else:
                left=mid+1

        return left