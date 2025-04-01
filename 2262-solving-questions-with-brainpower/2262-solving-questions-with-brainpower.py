class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            points,brainpower=questions[i]

            dp[i]=max(dp[i+1],points+(dp[i+brainpower+1] if i+brainpower+1<n else 0))

        return dp[0]