class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Two heaps to track min/max indices, sorted by nums[index]
        min_heap = []  # (nums[i], i) tuples for min tracking
        max_heap = []  # (-nums[i], i) tuples for max tracking
        left = right = 0
        count = 0

        while right < len(nums):
            # Add current index to both heaps
            # For max heap, negate value to convert min heap to max heap
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            # While window violates |nums[i] - nums[j]| ≤ 2
            # Shrink window from left and remove outdated indices
            while left < right and -max_heap[0][0] - min_heap[0][0] > 2:
                left += 1

                # Remove indices outside window from both heaps
                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)

            count += right - left + 1
            right += 1

        return count