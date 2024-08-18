class Solution:
    def isUgly(self, n: int) -> bool:
        while n>1:
            if n%5==0:
                n=n//5
            elif n%3==0:
                n=n//3
            elif n%2==0:
                n=n//2
            else:
                break
        return n==1