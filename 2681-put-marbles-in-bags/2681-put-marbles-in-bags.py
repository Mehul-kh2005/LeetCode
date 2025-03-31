class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        pairWeights=[weights[i]+weights[i+1] for i in range(n-1)]
        pairWeights.sort()

        ans=0
        for i in range(k-1):
            ans+=pairWeights[n-2-i]-pairWeights[i]

        return ans