class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        if n<3:
            return s

        s_list=list(s)
        j=2

        for i in range(2,n):
            if s_list[i]!=s_list[j-1] or s_list[i]!=s_list[j-2]:
                s_list[j]=s_list[i]
                j+=1

        return "".join(s_list[:j])