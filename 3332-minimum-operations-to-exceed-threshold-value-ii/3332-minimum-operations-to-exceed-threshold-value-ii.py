import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            new_ele = 2 * x + y
            heapq.heappush(nums, new_ele)
            count += 1

        if nums[0] < k:
            return -1

        return count