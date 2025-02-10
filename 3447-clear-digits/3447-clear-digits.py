class Solution:
    def clearDigits(self, s: str) -> str:
        ans=[]
        for char in s:
            if char.isdigit() and ans:
                ans.pop()
            else:
                ans.append(char)

        return "".join(ans)