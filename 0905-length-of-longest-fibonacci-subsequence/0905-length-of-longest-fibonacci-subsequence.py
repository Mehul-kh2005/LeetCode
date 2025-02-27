class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[0]*n for _ in range(n)]
        max_len=0

        for curr in range(2,n):
            start=0
            end=curr-1

            while start<end:
                pair_sum=arr[start]+arr[end]

                if pair_sum>arr[curr]:
                    end-=1
                elif pair_sum<arr[curr]:
                    start+=1
                else:
                    dp[end][curr]=dp[start][end]+1
                    max_len=max(max_len,dp[end][curr])
                    start+=1
                    end-=1

        return max_len+2 if max_len else 0