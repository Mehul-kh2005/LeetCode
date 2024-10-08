class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        to_remove=set()

        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        while stack:
            to_remove.add(stack.pop())

        for i,ch in enumerate(s):
            if i not in to_remove:
                stack.append(ch)

        return "".join(stack)