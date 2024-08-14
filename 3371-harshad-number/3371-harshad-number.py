class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        dsum = sum(map(int, str(x)))
        if x%dsum:
            return -1
        return dsum