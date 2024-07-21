class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        total = 0
        for i in range(len(s)-1):
            if s[i] == '1':
                total += 1
                if s[i+1] == '0':
                    ans += total
        return ans