class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result=[]
        for i in range(0,len(s),k):
            result.append(s[i:i+k])

        if len(result[-1])!=k:
            diff=k-len(result[-1])
            result[-1]+=fill*diff

        return result