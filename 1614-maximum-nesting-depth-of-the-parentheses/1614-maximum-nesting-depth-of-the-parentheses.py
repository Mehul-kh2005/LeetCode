class Solution:
    def maxDepth(self, s: str) -> int:
        left=0
        right=0
        result=0

        for ch in s:
            if ch=='(':
                left+=1

            elif ch==')':
                right+=1

            result=max(result,left-right)

        return result