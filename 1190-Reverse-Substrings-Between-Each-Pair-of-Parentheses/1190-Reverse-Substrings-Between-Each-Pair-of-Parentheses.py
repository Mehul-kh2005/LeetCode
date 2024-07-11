class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()  # remove the '(' from stack
                stack.extend(temp)  # add the reversed content back to the stack
            else:
                stack.append(char)
        
        return ''.join(stack)