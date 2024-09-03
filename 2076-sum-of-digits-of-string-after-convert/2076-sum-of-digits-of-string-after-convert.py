class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_string = ''.join(str(ord(char) - 96) for char in s)

        current_sum = sum(int(digit) for digit in numeric_string)
        
        for _ in range(k - 1):
            current_sum = sum(int(digit) for digit in str(current_sum))
        
        return current_sum