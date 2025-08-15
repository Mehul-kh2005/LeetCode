class Solution:
    def isPowerOfFour(self, n: int) -> bool:        
        if n <= 0:
            return False

        return  n.bit_length()%2 == 1 and n.bit_count() == 1