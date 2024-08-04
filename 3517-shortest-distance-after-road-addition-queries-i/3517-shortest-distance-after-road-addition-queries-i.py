class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        neigh = [[] for _ in range(n)]
        
        for i in range(1,n):
            neigh[i].append(i-1)

        inf = 10**9
            
        ans = []
        for [u,v] in queries:
            neigh[v].append(u)
            
            dp = [inf]*(n)
            dp[0] = 0
            for i in range(1,n):
                
                for pre in neigh[i]:
                    dp[i] = min(dp[i], dp[pre] + 1)
                    
            ans.append(dp[n-1])
            
        return ans