class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=str(x)
        l=[]
        for i in range(len(x1)):
            l.append(x1[i])
        l.reverse()
        x2=''.join(l)
        return x1==x2