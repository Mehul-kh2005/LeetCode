class Solution(object):
    def minCost(self, col, time):
        n, sum_ = len(col), 0
        for i in range(1, n):
            if col[i] == col[i - 1]:
                sum_ += min(time[i], time[i - 1])
                time[i] = max(time[i], time[i - 1])
        return sum_