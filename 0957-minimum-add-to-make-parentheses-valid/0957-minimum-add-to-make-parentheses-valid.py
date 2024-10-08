class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bracket=0
        required_bracket=0

        for ch in s:
            if ch=='(':
                open_bracket+=1
            else:
                if open_bracket>0:
                    open_bracket-=1
                else:
                    required_bracket+=1

        return open_bracket+required_bracket