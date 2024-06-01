class Solution:
    def tribonacci(self, n: int) -> int:
        t0=0
        t1=1
        t2=1
        for i in range(n):
            temp=t0
            t0=t1
            t1=t2
            t2=temp+t0+t1
        return t0