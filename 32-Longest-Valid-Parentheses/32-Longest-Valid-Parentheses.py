class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1] 
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len