class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for v in cnt.values():
            ans += (v - 1) % 2 + 1
        return ans