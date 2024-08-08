class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p,len_s=len(p),len(s)

        if len_p>len_s:
            return []

        p="".join(sorted(p))
        result=[]

        for i in range(0,len_s-len_p+1):
            word="".join(sorted(s[i:i+len_p]))
            if word==p:
                result.append(i) 
        
        return result