class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix_sums=[0]*(n+1)

        for i in range(1,n+1):
            prefix_sums[i]=prefix_sums[i-1]+nums[i-1]

        candidate_indices=deque()
        shortest_subarray_length=float('inf')

        for i in range(n+1):
            while candidate_indices and prefix_sums[i]-prefix_sums[candidate_indices[0]]>=k:
                shortest_subarray_length=min(shortest_subarray_length,i-candidate_indices.popleft())

            while candidate_indices and prefix_sums[i]<=prefix_sums[candidate_indices[-1]]:
                candidate_indices.pop()

            candidate_indices.append(i)

        return (shortest_subarray_length if shortest_subarray_length!=float('inf') else -1)