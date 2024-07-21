class Solution(object):
    def minChanges(self, n, k):
        # Step 1: Check if it's possible to convert n to k
        if (n & k) != k:
            return -1
        
        # Step 2: Count the number of 1 bits in n and k
        res = 0
        
        for c in bin(n)[2:]:
            res += int(c)
        
        for c in bin(k)[2:]:
            res -= int(c)
        
        # Step 3: Return the number of changes needed
        return res