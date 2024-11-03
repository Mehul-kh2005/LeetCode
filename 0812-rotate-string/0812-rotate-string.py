class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        doubled_string=s+s
        return doubled_string.find(goal)!=-1