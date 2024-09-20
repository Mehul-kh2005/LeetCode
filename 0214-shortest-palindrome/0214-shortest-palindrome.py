class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        reversed_string=s[::-1]

        for i in range(n):
            if s[:n-i]==reversed_string[i:]:
                return reversed_string[:i]+s

        return ""