class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        min_heap = []
        total_sum = 0
        
        # Generate all subarray sums
        for start in range(n):
            for end in range(start + 1, n + 1):
                subarray_sum = prefix_sums[end] - prefix_sums[start]
                if len(min_heap) < right:
                    heapq.heappush(min_heap, -subarray_sum)
                else:
                    if -min_heap[0] > subarray_sum:
                        heapq.heappushpop(min_heap, -subarray_sum)
        
        # Compute the sum of the range [left-1, right-1]
        min_heap = [-x for x in min_heap]
        heapq.heapify(min_heap)
        for _ in range(right - left + 1):
            total_sum += heapq.heappop(min_heap)
        
        return (total_sum + mod) % mod