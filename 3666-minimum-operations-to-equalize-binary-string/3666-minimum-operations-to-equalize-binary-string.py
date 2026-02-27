class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # O(n) time complexity
        # O(1) space complexity

        n = len(s)
        z = s.count('0')
        
        if n == k:
            if z == 0:
                return 0
            elif z == n:
                return 1
            else:
                return -1
        
        def ceil(x, y):
            return (x + y - 1) // y
        
        ans = inf
        
        if z % 2 == 0:
            m = max(ceil(z, k), ceil(z, n - k))
            if m % 2 == 1:
                m += 1
            ans = min(ans, m)
        
        if z % 2 == k % 2:
            m = max(ceil(z, k), ceil(n - z, n - k))
            if m % 2 == 0:
                m += 1
            ans = min(ans, m)
        
        return ans if ans < inf else -1