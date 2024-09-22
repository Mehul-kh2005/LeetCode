class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if k==1:
            return 1

        current=1
        k-=1

        while k>0:
            steps=0
            first=current
            last=current+1

            while first<=n:
                steps+=min(last,n+1)-first
                first*=10
                last*=10

            if steps<=k:
                current+=1
                k-=steps

            else:
                current*=10
                k-=1

        return current