class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans=count=0

        for char in s:
            if char=="b":
                count+=1
            elif count:
                ans+=1
                count-=1

        return ans