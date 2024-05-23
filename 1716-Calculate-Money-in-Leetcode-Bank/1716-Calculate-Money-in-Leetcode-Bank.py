class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range(n):
            week = i // 7  # Calculate which week it is
            day_in_week = i % 7 + 1  # Calculate which day in the week it is (1-indexed)
            total += week + day_in_week  # Add the amount of money for this day
        return total