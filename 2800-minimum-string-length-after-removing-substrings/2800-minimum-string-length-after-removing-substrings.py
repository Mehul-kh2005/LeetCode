class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for char in s:
            if not stack:
                stack.append(char)
                continue

            if char=="B" and stack[-1]=="A":
                stack.pop()

            elif char=="D" and stack[-1]=="C":
                stack.pop()

            else:
                stack.append(char)

        return len(stack)