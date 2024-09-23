class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        dictionary=set(dictionary)
        dp=[float("inf")]*(n+1)
        dp[n]=0

        for i in range(n-1,-1,-1):
            dp[i]=dp[i+1]+1

            for j in range(i+1,n+1):
                if s[i:j] in dictionary:
                    dp[i]=min(dp[i],dp[j])

        return dp[0]