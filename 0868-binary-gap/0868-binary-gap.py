class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        left = 0
        max_dist = 0

        while left < len(bin_n) and bin_n[left] == '0':
            left += 1
        
        for right in range(left + 1, len(bin_n)):
            if bin_n[right] == '1':
                max_dist = max(max_dist, right - left)
                left = right
        return max_dist