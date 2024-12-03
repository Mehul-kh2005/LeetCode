class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        dq=deque()
        spaces=set(spaces)

        for i in range(len(s)):
            if i in spaces:
                dq.append(" ")
            dq.append(s[i])

        return "".join(dq)