class Solution:
    def getSmallestString(self, s: str) -> str:
        list1=list(s)
        n=len(list1)
        min_string="".join(list1)
        
        for i in range(n-1):
            if int(list1[i])%2 == int(list1[i+1])%2:
                list1[i],list1[i+1]=list1[i+1],list1[i]
                
                new_string="".join(list1)
                min_string=min(min_string,new_string)
                
                list1[i],list1[i+1]=list1[i+1],list1[i]
        
        return min_string