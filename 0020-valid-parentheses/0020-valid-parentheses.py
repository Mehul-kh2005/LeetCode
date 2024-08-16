class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing to opening parentheses
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Pop from stack if it matches the top of the stack
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # Push the opening parenthesis onto the stack
                stack.append(char)
        
        # If stack is empty, all parentheses matched
        return not stack