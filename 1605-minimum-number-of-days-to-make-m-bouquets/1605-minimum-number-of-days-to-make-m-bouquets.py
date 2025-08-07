class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isPossible(curr_day):
            count=0
            num_bouquets=0

            for day in bloomDay:
                if curr_day>=day:
                    count+=1

                else:
                    num_bouquets+=(count//k)
                    count=0
                    
            num_bouquets+=(count//k)

            return num_bouquets>=m

        n=len(bloomDay)
        if n<m*k:
            return -1

        left=min(bloomDay)
        right=max(bloomDay)

        while left<=right:
            mid=(left+right)//2

            if isPossible(mid): 
                right=mid-1

            else:
                left=mid+1

        return left