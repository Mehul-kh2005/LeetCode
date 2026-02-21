class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth=0
        result=""

        for ch in s:
            if ch=='(':
                depth+=1
                if depth>1:
                    result+=ch

            else:
                depth-=1
                if depth>0:
                    result+=ch

        return result          