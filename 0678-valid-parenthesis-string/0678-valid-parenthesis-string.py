class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  
        max_open = 0 
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                min_open -= 1  # Treat '*' as ')'
                max_open += 1  # Treat '*' as '('
            
            if max_open < 0:
                return False  # More ')' than '(' possible at this point
            
            if min_open < 0:
                min_open = 0  # Reset min_open to 0 if it goes negative
        
        return min_open == 0