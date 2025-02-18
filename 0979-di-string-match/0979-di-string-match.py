class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result=[]
        stack=[]

        for i in range(len(s)+1):
            stack.append(i)

            if i==len(s) or s[i]=="I":
                while stack:
                    result.append(stack.pop())

        return result