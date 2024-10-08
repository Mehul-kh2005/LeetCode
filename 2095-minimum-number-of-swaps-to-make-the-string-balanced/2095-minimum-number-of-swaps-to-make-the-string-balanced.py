class Solution:
    def minSwaps(self, s: str) -> int:
        stackSize=0
        for ch in s:
            if ch=='[':
                stackSize+=1
            elif ch==']' and stackSize>0:
                stackSize-=1
        return (stackSize+1)//2