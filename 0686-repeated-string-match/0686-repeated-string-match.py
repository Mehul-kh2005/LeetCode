class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_reps = -(-len(b) // len(a))  # Ceiling division
        
        # Check if b is a substring of the repeated a string
        if b in a * min_reps:
            return min_reps
        
        # Check the next repetition to cover edge cases
        if b in a * (min_reps + 1):
            return min_reps + 1
        
        # If b is not found in the repeated a string
        return -1