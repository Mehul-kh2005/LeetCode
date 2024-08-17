class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cols = len(points[0])
        current_row = [0] * cols
        previous_row = [0] * cols

        for row in points:
            # running_max holds the maximum value generated in the previous iteration of each loop
            running_max = 0

            # Left to right pass
            for col in range(cols):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = running_max

            running_max = 0
            # Right to left pass
            for col in range(cols - 1, -1, -1):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = max(current_row[col], running_max) + row[col]

            # Update previous_row for next iteration
            previous_row = current_row.copy()

        # Find maximum points in the last row
        return max(previous_row)