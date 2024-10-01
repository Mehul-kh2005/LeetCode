from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count=Counter(x%k for x in arr)

        if remainder_count[0]%2!=0:
            return False

        for i in range(1,(k//2)+1):
            if remainder_count[i]!=remainder_count[k-i]:
                return False

        if k%2==0 and remainder_count[k//2]%2!=0:
            return False

        return True