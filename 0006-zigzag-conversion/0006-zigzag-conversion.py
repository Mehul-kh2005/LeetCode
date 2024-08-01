class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1 or greater than or equal to the length of s, return s
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = ['' for _ in range(numRows)]
        current_row = 0
        going_down = False

        # Build the zigzag pattern
        for char in s:
            rows[current_row] += char
            # Change direction if we are at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row
            current_row += 1 if going_down else -1

        # Join all rows to get the final string
        return ''.join(rows)