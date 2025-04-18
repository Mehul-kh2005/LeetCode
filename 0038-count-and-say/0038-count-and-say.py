class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"

        prev="1"
        
        for _ in range(2,n+1):
            i=0
            result=""
            
            while i<len(prev):
                count=1
                while i+1<len(prev) and prev[i]==prev[i+1]:
                    count+=1
                    i+=1
                    
                result+=str(count)+prev[i]
                i+=1

            prev=result

        return prev