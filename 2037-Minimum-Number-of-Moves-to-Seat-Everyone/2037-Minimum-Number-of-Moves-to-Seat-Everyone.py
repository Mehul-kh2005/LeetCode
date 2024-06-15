class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Find the maximum position in the arrays
        max_position = max(max(seats), max(students))

        # Stores difference between number of seats and students at each position
        differences = [0] * (max_position)

        # Count the available seats at each position
        for position in seats:
            differences[position - 1] += 1

        # Remove a seat for each student at that position
        for position in students:
            differences[position - 1] -= 1

        # Caculate the number of moves needed to seat the students
        moves = 0
        unmatched = 0
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference

        return moves