class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        count=sum=0

        for i in range(1,n+1):
            if i not in banned and sum+i<=maxSum:
                sum+=i
                count+=1

        return count