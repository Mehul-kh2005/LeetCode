class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def parenthesis(left,right,s):
            if len(s)==n*2:
                result.append(s)
                return

            if left<n:
                parenthesis(left+1,right,s+"(")

            if right<left:
                parenthesis(left,right+1,s+")")

        result=[]
        parenthesis(0,0,"")
        return result