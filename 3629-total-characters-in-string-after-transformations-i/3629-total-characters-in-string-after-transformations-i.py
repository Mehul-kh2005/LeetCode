class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod_val=1000000007
        dq=deque([0]*26)
        a=ord('a')
        
        for char in s:
            dq[ord(char)-a]+=1
        
        for i in range(t):
            z=dq.pop()
            dq.appendleft(z)
            dq[1]+=z

        return sum(dq)%mod_val