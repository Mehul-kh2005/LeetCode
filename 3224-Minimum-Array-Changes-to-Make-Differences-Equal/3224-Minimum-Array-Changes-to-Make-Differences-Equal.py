class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        n //= 2
        diff = Counter()
        for i in range(n):
            x = nums[i]
            y = nums[-i-1]
            v = abs(x - y)
            diff[v] -= 1
            diff[v+1] += 1
            v = max(x, k - x, y, k - y)
            diff[0] += 1
            diff[v+1] += 1
            diff[k+1] -= 1
        cur = 0
        ans = n * 2
        for x in sorted(diff):
            cur += diff[x]
            if x <= k:
                ans = min(ans, cur)
        return ans