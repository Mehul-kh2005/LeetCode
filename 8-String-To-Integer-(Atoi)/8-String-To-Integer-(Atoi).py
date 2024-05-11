class Solution:
    def myAtoi(self, s: str) -> int:
        result=0
        sign=1
        i=0
        
        while i<len(s) and s[i]==" ":
            i+=1
        
        if i<len(s) and (s[i]=="+" or s[i]=="-"):
            if s[i]=="-":
                sign=-1
            i+=1
        
        while i<len(s) and s[i].isdigit() :
            result=result*10+int(s[i])
            i+=1
        
        result*=sign

        return max(min(result, 2**31 - 1), -2**31)