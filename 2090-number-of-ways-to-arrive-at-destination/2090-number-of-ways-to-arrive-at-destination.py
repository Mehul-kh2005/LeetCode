class Solution:
    MOD = 1_000_000_007

    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for src in range(n):
            for dest in range(n):
                if src != dest:
                    dp[src][dest][0] = int(1e12)
                    dp[src][dest][1] = 0
                else:
                    dp[src][dest][0] = 0
                    dp[src][dest][1] = 1

        for start_node, end_node, travel_time in roads:
            dp[start_node][end_node][0] = travel_time
            dp[end_node][start_node][0] = travel_time
            dp[start_node][end_node][1] = 1
            dp[end_node][start_node][1] = 1

        for mid in range(n):
            for src in range(n):
                for dest in range(n):
                    if src != mid and dest != mid:
                        new_time = dp[src][mid][0] + dp[mid][dest][0]

                        if new_time < dp[src][dest][0]:
                            dp[src][dest][0] = new_time
                            dp[src][dest][1] = (
                                dp[src][mid][1] * dp[mid][dest][1]
                            ) % self.MOD
                        elif new_time == dp[src][dest][0]:

                            dp[src][dest][1] = (
                                dp[src][dest][1]
                                + dp[src][mid][1] * dp[mid][dest][1]
                            ) % self.MOD

        return dp[n - 1][0][1]